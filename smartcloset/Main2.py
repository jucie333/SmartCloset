import cvzone
import cv2
from cvzone.PoseModule import PoseDetector
import os
import cv2
import socket
import pickle
import struct

global imageNumber, rgb_color
imageNumber = 1

# 소켓 설정
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))  # MagicMirror 모듈의 서버 주소

# 버튼 클릭을 처리하는 함수
def on_button_click(event, x, y, flags, param):
    buttons, callback = param

    if event == cv2.EVENT_LBUTTONDOWN:
        for button, action in buttons.items():
            x_start, y_start, x_end, y_end = button
            if x_start < x < x_end and y_start < y < y_end:
                callback(action)


# 버튼을 그리는 함수
def draw_buttons(frame, buttons):
    global imageNumber
    count = 0
    rgb_color = (255, 0, 0)
    clicked_color = (255, 0, 0)

    for button, value in buttons.items():
        if count-1 == imageNumber:
            button_color = clicked_color
        else:
            button_color = rgb_color
        x_start, y_start, x_end, y_end = button
        cv2.rectangle(frame, (x_start, y_start), (x_end, y_end), button_color, 2)
        cv2.putText(x_start + 1, value, (x_start+ 10, y_end - y_start), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        count += 1


buttons = {
        (50, 1700, 200, 1750): "다음",
        (250, 1700, 400, 1750): "이미지1",
        (450, 1700, 600, 1750): "이미지2",
        (650, 1700, 800, 1750): "이미지3",
        (850, 1700, 1000, 1750): "이전",
    }


def capture_video(callback):
    global imageNumber, rgb_color
    cap = cv2.VideoCapture(0)
    detector = PoseDetector()

    shirtFolderPath = "Resources/Shirts"
    listShirts = os.listdir(shirtFolderPath)
    fixedRatio = 262 / 190
    shirtRatioHeightWidth = 581 / 440
    imageNumber = 4

    # 원하는 크기로 동영상 크기 조정
    desired_width = 800
    desired_height = 500

    # 동영상 크기 조정
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)
    while True:
        success, img = cap.read()



        # 비디오가 마지막 프레임에 도달하면 다시 시작
        if not success:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue
        draw_buttons(img, buttons)
        img = detector.findPose(img)
        lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
        if lmList:
            lm11 = lmList[11][1:3]
            lm12 = lmList[12][1:3]
            imgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[imageNumber]), cv2.IMREAD_UNCHANGED)

            widthOfShirt = int((lm11[0] - lm12[0]) * fixedRatio)
            widthOfShirt = -100
            print("width : "+ str(widthOfShirt))
            if widthOfShirt > 0 and int(widthOfShirt * shirtRatioHeightWidth) > 0:
                imgShirt = cv2.resize(imgShirt, (widthOfShirt, int(widthOfShirt * shirtRatioHeightWidth)))

            currentScale = (lm11[0] - lm12[0]) / 190
            offset = -40, -380
            try:
                img = cvzone.overlayPNG(img, imgShirt, (lm12[0] - offset[0], lm12[1] - offset[1]))
            except:
                pass

        cv2.imshow("Image", img)
        data = pickle.dumps(img)
        try:
            # 데이터 전송
            client_socket.sendall(struct.pack(">L", size) + data)
        except:
            break

        cv2.setMouseCallback('Image', on_button_click, (buttons, callback))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    client_socket.close()

# 버튼을 클릭할 때 호출되는 콜백 함수
def button_callback(action):
    global imageNumber
    if action == "이미지1":
        imageNumber = 1

    elif action == "이미지2":
        imageNumber = 2
    elif action == "이미지3":
        imageNumber = 3
    print(imageNumber)
    print(f"Button '{action}' was clicked!")



# 모듈을 시작할 때 호출하는 함수
def start_module():
    capture_video(button_callback)


# 모듈 시작
if __name__ == "__main__":
    start_module()
