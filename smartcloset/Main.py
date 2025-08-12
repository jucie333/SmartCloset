import cvzone
import cv2
from cvzone.PoseModule import PoseDetector
import os

cap = cv2.VideoCapture("./test.avi")
detector = PoseDetector()

shirtFolderPath = "Resources/Shirts"
listShirts = os.listdir(shirtFolderPath)
fixedRatio = 262/190
shirtRatioHeightWidth = 581/440
imageNumber = 1

while True:
    success, img = cap.read()

    # 비디오가 마지막 프레임에 도달하면 다시 시작
    if not success:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
    if lmList:
        lm11 = lmList[11][1:3]
        lm12 = lmList[12][1:3]
        imgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[imageNumber]), cv2.IMREAD_UNCHANGED)

        widthOfShirt = int((lm11[0] - lm12[0]) * 1.5)
        if widthOfShirt > 0:
            imgShirt = cv2.resize(imgShirt, (widthOfShirt, int(widthOfShirt * shirtRatioHeightWidth)))

            offset = (-int(widthOfShirt * 0.4), -int(widthOfShirt * 0.6))  # 이동 오프셋 수정
            try:
                img = cvzone.overlayPNG(img, imgShirt, (int(lm12[0]) + offset[0], int(lm12[1]) + offset[1]))
            except:
                pass

    cv2.imshow("Image", img)
    cv2.waitKey(1)
