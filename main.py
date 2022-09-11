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

#start live detection if start button is clicked
#object_name = 'object_name'
@app.route('/live', methods=['GET', 'POST']) #a tab to display converted bytes video
def live():
    if request.method == 'POST':
        #fetch results from live detection
        object = detection_result()
        #return results in dictionary passed to load.html
        image_suggestions = search_image(object)
        print(image_suggestions)
        #return render_template('load.html', image_suggestions=image_suggestions)
    return render_template('live.html')
    #camera works

#search nearby recycling centers, retrives user's location first
'''
#call functions from api_queries.py and update dictionary recycling places with information
#includes at most 10 recycling places
global recycling_places 
'''
@app.route('/location_search', methods=['GET', 'POST'])
def location_search():
    if request.method == 'POST':
        #python dictionary for locations #prototype
        location_examples = {"Ranch Town Recycling Center Inc":{"website":"https://www.ranchtownrecycling.com/",
                                                            "address":"775 Lincoln Ave, San Jose, CA 95126",
                                                            "distance":"6.1 miles"},
                            "Story Road Recycling LLC":{"website":"http://storyroadrecycling.com/",
                                                            "address":"1303 Story Rd, San Jose, CA 95122",
                                                            "distance":"10.8 miles"},
                            "ASC Recycling":{"website":"https://www.ascrecycling.com/",
                                                            "address":"1970 Monterey Rd, San Jose, CA 95112",
                                                            "distance":"10.3 miles"},
                            "Schnitzer":{"website":"https://www.schnitzersteel.com/locations/144",
                                                            "address":"11665 Berryessa Rd, San Jose, CA 95133",
                                                            "distance":"8.3 miles"},
                            "Jado Recycling":{"website":"http://www.jadorecycling.com/ ",
                                                            "address":"4650 Meridian Ave, San Jose, CA 95124",
                                                            "distance":"9.5 miles"}}
        #return new page
        return render_template('location_search.html', location_examples=location_examples)
    return render_template('location_search.html')

#run the app
if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(debug = True) #to be removed after done with all coding above