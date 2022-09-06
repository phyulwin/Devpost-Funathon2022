import re, os
from flask import Flask, render_template, request, redirect, url_for, Response
import cv2
import numpy as np
from cv2LiveDetection import livedetection, detection_result

#import functions from other python files
from api_queries import search_image, getUserLocation

app = Flask(__name__)

@app.route('/video_feed') #just a route to convert cv2 video to web byte stream (idk how else to do it)
def video_feed():
    return Response(livedetection(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

#start live detection if start button is clicked #TODO
@app.route('/live', methods=['GET', 'POST']) #a tab to display converted bytes video
def live():

    # #detect object
    # livedetection()
    # if request.method == 'GET':
    #     #object_name = live_detection() get object name and call queries
    #     pass
    return render_template('live.html')

@app.route('/load', methods=['GET', 'POST']) #the screen with the final img and label (supposedly)
def load():

    if request.method == 'GET':
        result_img, object_name = detection_result() 
        print('ppp' + object_name)

    return render_template('load.html')

#search nearby recycling centers, retrives user's location first #TODO
@app.route('/location_search', methods=['GET', 'POST'])
def location_search():
    if request.method == 'GET':
        '''
        #call functions from api_queries.py and update dictionary recycling places with information
        #includes at most 10 recycling places
        global recycling_places 
        '''
        #return new page
        return render_template('location_search.html')
    return render_template('location_search.html')






#run the app
if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(debug = True) #to be removed after done with all coding above