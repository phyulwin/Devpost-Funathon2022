import re, os
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

#pip install opencv-python tensorflow
#pip install cvlib

img = ""

def livedetection():

    # open webcam
    webcam = cv2.VideoCapture(0)

    if not webcam.isOpened():
        print("Could not open webcam")
        exit()
        

    # loop through frames
    while webcam.isOpened():

        # read frame from webcam 
    # read frame from webcam 
        # read frame from webcam 
        status, frame = webcam.read()

        if not status:
            print("Could not read frame")
            exit()

        # apply object detection
        bbox, label, conf = cv.detect_common_objects(frame, confidence=0.25, model='yolov4-tiny')


        print(label)

        if 'person' in label:
            bbox.pop(label.index('person'))
            conf.pop(label.index('person'))
            label.pop(label.index('person'))

        if 'person' in label:
            bbox.pop(label.index('person'))
            conf.pop(label.index('person'))
            label.pop(label.index('person'))
        
        # draw bounding box over detected objects
        out = draw_bbox(frame, bbox, label, conf)
        img = out

        # display output
        cv2.imshow("Real-time object detection", out)

        # press "Q" to stop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            
            # release resources
            webcam.release()
            cv2.destroyAllWindows()
            return label[0], out
        

def show_detected():
    thing, img = livedetection()
    cv2.imshow('detected', img)
    cv2.waitKey(0)


#show_detected()



