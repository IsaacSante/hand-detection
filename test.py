import cv2
#print(cv2.__version__)

### Run webcam 
frameWidth = 640
frameHeight = 480 
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# when program is done, release the capture 
cap.release()
cv2.destroyAllWindows()
