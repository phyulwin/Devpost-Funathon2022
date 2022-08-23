#api_queries.py
#receives object name as string value from main.py
#make queries to api and return results as images, videos, articles and blogs links
import re,os
import requests

#call for api
'''
Google Image Search API
https://rapidapi.com/Glavier/api/google-image-search1/
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
    #testing article links return -> print(article_link)