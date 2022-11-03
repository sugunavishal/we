import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")

# Load tracker 
tracker = cv2.TrackerCSRT_create()

# Read the first frame of the video
returned, img = video.read()

# Select the bounding box on the image
bbox = cv2.selectROI("Tracking", img, False)

# Initialise the tracker on the img and the bounding box
tracker.init(img, bbox)

print(bbox)
def drawbox(img,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),(x+w),(y+h),(2,255,55),3)
    cv2.putText(img,"ball track",(100,150),cv2.FONT_ITALIC,0.7,(66,222,111),3)



while True:
    check,img = video.read()
    success,bbox=tracker.update(img)   
    if success:
        drawbox(img,bbox)

            
    else:
        cv2.putText(img,"lost",(100,150),cv2.FONT_ITALIC,0.7,(66,222,111),3)

    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()







