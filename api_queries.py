#api_queries.py
#API headers are different for each API
import re,os
import requests
import socket

#call for api - getUserLocation() and suggest_locations() functions are not used in this demo
'''
Google Image Search API
https://rapidapi.com/Glavier/api/google-image-search1/

#receives object name as string value from main.py
#make queries to api and return results as images, videos, articles and blogs links
'''
def search_image(detected_obj):
  url = "https://google-image-search1.p.rapidapi.com/v2/"
  querystring = {"q":detected_obj}
  #API KEY from rapidapi.com; to be hidden if the code is shared to github public
  headers = {
  	"X-RapidAPI-Key": "a30b37ef15mshb61f4b1012a4f18p110da0jsn0b7954f3ca94",
  	"X-RapidAPI-Host": "google-image-search1.p.rapidapi.com"
  }
  response = requests.request("GET", url, headers=headers, params=querystring)
  response = response.json() #parse response

  #list of images found for the given search 
  image_suggestions = response['response']['images']
  return image_suggestions
  
'''
Google Maps Autocomplete Plus API
https://rapidapi.com/letscrape-6bRBa3QguO5/api/google-maps-autocomplete-plus/

the input parameters are user's latitude and longitude
'''
def suggest_locations(latitude,longitude):
  API_url = "https://google-maps-autocomplete-plus.p.rapidapi.com/autocomplete"
  #coordinates - Geographic coordinates from which the query is made. Recommended to use so that results are biased towards this location.
  coordinates = str(latitude) + "," + str(longitude)
  querystring = {"query":"shop","limit":"20","region":"us","language":"en","coordinates":coordinates}
  #include headers
  headers = {
    "X-RapidAPI-Key": "a30b37ef15mshb61f4b1012a4f18p110da0jsn0b7954f3ca94",
    "X-RapidAPI-Host": "google-maps-autocomplete-plus.p.rapidapi.com"
  }
  response = requests.request("GET", API_url, headers=headers, params=querystring)
  #print(response.text)
  response = response.json()

  #python list for predictions
  predictions = response['response']['predictions']
  for items in predictions:
    #main_text - The main part of the description (the bold part as seen on Google Maps site autocomplete).
    main_text = items['main_text']
    #description - Full prediction description.
    description = items['description']
    #print(main_text + ": " + description)
    
    coordinatesFound = True
    try:
      #item (location) latitude and longitude
      latitude = items['latitude']
      longitude = items['longitude']
    except:
      coordinatesFound = False
      
    #place_google_id - The unique Google Id of the matched Place. An example use is to use the Google Maps Search or Scraper APIs.
      placeGoogleIDFound = True
    try:
      google_id = items['place_google_id']
    except:
      placeGoogleIDFound = False
    #print('\n')
    
'''
IP Location API
https://rapidapi.com/ai-box-ai-box-default/api/ip-location5/

get user's city, state, and country
'''
def getUserLocation():
  #https://rapidapi.com/ai-box-ai-box-default/api/ip-location5/
  url = "https://ip-location5.p.rapidapi.com/get_geo_info"

  #get user IP address using socket module
  host_name = socket.gethostname()    
  IPAddress = socket.gethostbyname(host_name)
  payload = "ip=" + str(IPAddress)

  #include API key in headers
  headers = {
  	"content-type": "application/x-www-form-urlencoded",
  	"X-RapidAPI-Key": "a30b37ef15mshb61f4b1012a4f18p110da0jsn0b7954f3ca94",
  	"X-RapidAPI-Host": "ip-location5.p.rapidapi.com"
  }
  response = requests.request("POST", url, data=payload, headers=headers)
  response = response.json()

  try:
    #get user's latitude and longitude
    latitude = response['latitude']
    longitude = response['longitude']

    #call another API to search for nearby recycling centers
    suggest_locations(latitude,longitude)
    #return html with data
  except:
    #return html and manually ask user for input
    print("cannot get user's location or nearby recycling center info")
