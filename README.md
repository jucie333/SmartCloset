Smart Closet

프로젝트 개요

이 프로젝트는 웹캠으로 캡처한 비디오 스트림에서 사용자의 포즈를 감지하고, MagicMirror² 모듈을 통해 실시간으로 셔츠 이미지를 오버레이하여 표시합니다. 또한, 사용자 인터랙션을 위해 화면에 버튼을 추가하여 이미지 변경 등의 기능을 제공합니다.

주요 기능

	•	포즈 감지: 사용자의 포즈를 감지하여 주요 신체 포인트를 추적합니다.
	•	이미지 오버레이: 감지된 포즈를 기반으로 셔츠 이미지를 사용자의 몸에 오버레이합니다.
	•	실시간 전송: 처리된 이미지를 소켓을 통해 MagicMirror² 모듈에 전송합니다.
	•	사용자 인터랙션: 화면에 버튼을 추가하여 이미지 변경 등의 기능을 제공합니다.

기술 스택

	•	Python: OpenCV, cvzone, PoseDetector
	•	JavaScript: MagicMirror² 모듈
	•	Socket: 소켓을 이용한 서버-클라이언트 통신

참고 자료

	•	OpenCV Documentation
	•	MagicMirror² Documentation
	•	cvzone GitHub Repository

 <img width="1414" alt="스크린샷 2024-07-06 오후 9 36 35" src="https://github.com/Limchaereong/SmartCloset/assets/159234510/cd548670-86be-48fd-9369-9c7eead62dac">
<img width="1415" alt="스크린샷 2024-07-06 오후 9 36 46" src="https://github.com/Limchaereong/SmartCloset/assets/159234510/9cf6bb61-fdab-49c0-89ce-3121d692706d">
<img width="1407" alt="스크린샷 2024-07-06 오후 9 36 54" src="https://github.com/Limchaereong/SmartCloset/assets/159234510/c9756def-82ab-472f-9046-3477535bf90f">
