import cv2
from tracker import *


# # Create tracker object
tracker = EuclideanDistTracker()

# Read the video from specified path
currentframe = 0
cap = cv2.VideoCapture("E:\dafcsdf\IMG_0427.MOV")

object_detector = cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=30)

while True:
    ret, frame = cap.read()

    height=1920
    width=1080
    # Extract Region of interest
    roi = frame[50: 800,200: 1800]
    # 1. Object Detection
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    count =0
    mark=True
    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > 5000:
            # cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi,(x,y),(x+w , y+h),(0,255,0),3)
            detections.append([x, y, w, h])
            if(len(detections)>5 & mark):
               count=count+1
               print(len(detections))
               name = './images/' + str(currentframe) + '.jpg'
               print('Creating...' + name)

               isWritten = cv2.imwrite(f'F:\SEM-5 MATRIAL\CN\PPT\lpw prep\hackathon_files\images\{name}', frame)

               if isWritten:
                   print('The image is successfully saved.')

               cv2.imwrite(name, frame)
               currentframe += 1
               mark=False

            if(len(detections)<3):
                mark=True




    print(detections)
    cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
print(count)




