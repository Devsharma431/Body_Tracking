import cv2
import mediapipe
import time

cap = cv2.VideoCapture("hello woeld.mp4")
pTime = 0
mpdraw = mediapipe.solutions.drawing_utils
mpose = mediapipe.solutions.pose
pose = mpose.Pose()
while True:
    succes, img = cap.read()
    image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    results = pose.process(image)
    print(results.pose_landmarks)
    if results.pose_landmarks:
        mpdraw.draw_landmarks(img, results.pose_landmarks, mpose.POSE_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    cv2.imshow("IMAGE", img)
    cv2.waitKey(1)