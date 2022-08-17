#import libraries
import re, os
from flask import Flask, render_template, request, redirect, url_for, Response
import cv2
import numpy as np

#import functions from other python files
from cv2LiveDetection import live_detection
#from api_queries import functions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#start live detection if start button is clicked #TODO
@app.route('/live', methods=['GET', 'POST'])
def live():
    if request.method == 'GET':
        #start video capture
        camera = cv2.VideoCapture(0)
        #detect object
        live_detection()
        #object_name = live_detection() get object name and call queries
    return render_template('load.html')






#run the app
if __name__ == "__main__":
    app.run()