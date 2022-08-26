import re, os
from flask import Flask, render_template, request, redirect, url_for, Response
import cv2
import numpy as np

#import functions from other python files
from cv2LiveDetection import show_detected
from api_queries import search_image, getUserLocation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#start live detection if start button is clicked #TODO
@app.route('/live', methods=['GET', 'POST'])
def live():
    #detect object
    show_detected()
    if request.method == 'GET':
        #object_name = live_detection() get object name and call queries
        pass
    return render_template('load.html')

#search nearby recycling centers, retrives user's location first #TODO
@app.route('/location_search', methods=['GET', 'POST'])
def location_search():
    if request.method == 'GET':
        getUserLocation()

        #return new page
        return render_template('location_search.html')
    return render_template('location_search.html')






#run the app
if __name__ == "__main__":
    app.run()