import cv2
import mediapipe as mp

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                if id == 4:
                    cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                if id == 8:
                    cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                if id == 12:
                    cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                if id == 16:
                    cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                if id == 20:
                    cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    fingers = []
    if results.multi_hand_landmarks:
        myHand = results.multi_hand_landmarks[0]
        for id, lm in enumerate(myHand.landmark):
            # print(id, lm)
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            if id == 4:
                fingers.append(1) if cy < 250 else fingers.append(0)
            if id == 8:
                fingers.append(1) if cy < 250 else fingers.append(0)
            if id == 12:
                fingers.append(1) if cy < 250 else fingers.append(0)
            if id == 16:
                fingers.append(1) if cy < 250 else fingers.append(0)
            if id == 20:
                fingers.append(1) if cy < 250 else fingers.append(0)

    fingerCount = fingers.count(1)
    cv2.putText(img, str(fingerCount), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()