#api_queries.py
import re,os
import requests
import socket

#call for api
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
  for each_image in image_suggestions:
    #source article about the image
    article_name = each_image['source']['title']
    article_link = each_image['source']['page']
    #image url
    image_url = each_image['image']['url']
    
    #testing image return -> print(image_url)

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
  payload = "ip=" + IPAddress

  #include API key in headers
  headers = {
  	"content-type": "application/x-www-form-urlencoded",
  	"X-RapidAPI-Key": "a30b37ef15mshb61f4b1012a4f18p110da0jsn0b7954f3ca94",
  	"X-RapidAPI-Host": "ip-location5.p.rapidapi.com"
  }
  response = requests.request("POST", url, data=payload, headers=headers)
  response = response.json()

  try:
    #get user's city, state, and country
    country = response['country']['name']
    state_region = response['region']
    city = response['city']
    print(country + " " + state_region + " " + city)

    #call another API to search for nearby recycling centers
    #TODO
    #return html with data
  except:
    #return html and manually ask user for input
    print("enter city and state: ")
