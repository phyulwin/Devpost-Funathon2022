import re, os
from flask import Flask, render_template, request, redirect, url_for, Response
import cv2
import numpy as np
from cv2LiveDetection import livedetection, detection_result

#import functions from other python files
from api_queries import search_image, getUserLocation

app = Flask(__name__)
times_scanned = 0 #this is a global variable for number of times scanned

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
    times_scanned = 8 #for desmonstration
    return render_template('live.html', times_scanned=times_scanned)

@app.route('/load', methods=['GET', 'POST'])
def load_results():
    #fetch results from live detection
    object = detection_result()
    #return results in dictionary passed to load.html
    object_results = "how to recycle" + str(object)
    image_suggestions = search_image(object_results)
    for each_image in image_suggestions:
        #source article about the image
        article_name = each_image['source']['title']
        article_link = each_image['source']['page']
        #image url
        image_url = each_image['image']['url']
    return render_template('load.html', image_suggestions=image_suggestions, object=object)

@app.route('/item_manual_search', methods=['GET', 'POST'])
def manual_search():
    #return results in dictionary passed to load.html
    object = request.form.get("input_item")
    object_results = "how to recycle" + str(object)
    image_suggestions = search_image(object_results)
    return render_template('load.html', image_suggestions=image_suggestions, object=object)

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
    app.run() #app running on http://127.0.0.1:5000/
    app.run(debug = True) #to be removed after done with all coding above