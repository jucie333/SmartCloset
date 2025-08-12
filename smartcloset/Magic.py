import cv2
import numpy as np


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
    for button in buttons.keys():
        x_start, y_start, x_end, y_end = button
        cv2.rectangle(frame, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)


# 카메라로 영상을 캡처하는 메인 함수
def capture_video(callback):
    cap = cv2.VideoCapture(0)

    buttons = {
        (50, 400, 150, 450): "다음",
        (200, 400, 300, 450): "이미지1",
        (350, 400, 450, 450): "이미지2",
        (500, 400, 600, 450): "이미지3",
        (650, 400, 750, 450): "이전",
    }

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        draw_buttons(frame, buttons)
        cv2.imshow('Magic Mirror', frame)

        cv2.setMouseCallback('Magic Mirror', on_button_click, (buttons, callback))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# 버튼을 클릭할 때 호출되는 콜백 함수
def button_callback(action):
    print(f"Button '{action}' was clicked!")


# 모듈을 시작할 때 호출하는 함수
def start_module():
    capture_video(button_callback)


# 모듈 시작
if __name__ == "__main__":
    start_module()
