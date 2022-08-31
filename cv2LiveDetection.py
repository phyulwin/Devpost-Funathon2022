import re, os
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

#pip install opencv-python tensorflow
#pip install cvlib

def livedetection():

    # open webcam
    webcam = cv2.VideoCapture(0)

    if not webcam.isOpened():
        print("Could not open webcam")
        exit()
        

    # loop through frames
    while webcam.isOpened():

        # read frame from webcam 
        status, frame = webcam.read()

        if not status:
            print("Could not read frame")
            exit()

        # apply object detection
        bbox, label, conf = cv.detect_common_objects(frame, confidence=0.25, model='yolov4-tiny')


        print(label)

        # removes any possible detection of a person
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
            return label[0], out # returns string of object, img of the selected frame
        
    # runs the detection, when finds the labeled object desired press q to lock it
    # then it shows another img of what is locked

def show_detected():
    thing, img = livedetection()
    cv2.imshow('detected', img)
    cv2.waitKey(0)


#show_detected() #test run

# some issues:
#     - the detection only expects exactly one item, if there are multiple or none then it goes out of bounds
#         - might have to have an exception error + visual notification thrown for that
#     - glitchy and slightly inaccurate
#     - not exactly sure how i want the method to work but it basically functions 




