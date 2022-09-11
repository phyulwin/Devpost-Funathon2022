import re, os
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

#pip install opencv-python tensorflow
#pip install cvlib

global img, obj_name

def livedetection(): # takes in camera, captures each frame, and then converts to byte to stream on web

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

        if 'person' in label:
            bbox.pop(label.index('person'))
            conf.pop(label.index('person'))
            label.pop(label.index('person'))
        
        # draw bounding box over detected objects
        out = draw_bbox(frame, bbox, label, conf)
        img = out
        obj_name = label

        # display output
        ret, buffer = cv2.imencode('.jpg', out)
        byteframe = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + byteframe + b'\r\n')

           
def detection_result(): 
    #there has to be a better way but i made global variables of the info 
    # i wanted to keep from the previous method, trying to save them like a snapshot
    # but i dont think it works unless i set up a class or smt
    obj_name = 'coca cola bottle'
    #return img, obj_name
    return obj_name
    #return label[0], out # returns string of object, img of the selected frame
        
    
    
# some issues:
#     - the detection only expects exactly one item, if there are multiple or none then it goes out of bounds
#         - might have to have an exception error + visual notification thrown for that
#     - glitchy and slightly inaccurate
#     - not exactly sure how i want the method to work but it basically functions 




