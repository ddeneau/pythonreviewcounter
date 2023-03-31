import googlemaps
import json
import requests
from datetime import datetime

counter = 0
# Replace key='[insert your key without brackets]'
gmaps = googlemaps.Client(key='AIzaSyDDKS_pV3ihaftl-2JRVEpqMlOZe8I0yp4')
# Specify the place ID of the business
place_id = 'ChIJ7fLdskyTToYR81Dj4KgYsds'
# Get the place details, including the reviews
place_details = gmaps.place(place_id, fields=['reviews'])
place_name = gmaps.place(place_id, fields=['name'])['result']['name']
# Extract the reviews
reviews = place_details['result']['reviews']

# Print the reviews
for review in reviews:
    counter = counter + 1
    print('Author:', review['author_name'])
    print('Rating:', review['rating'])
    print('Time:', datetime.fromtimestamp(review['time']))

print(place_name + " Number of Reviews: "+str(counter))
requests.put('https://polar-fortress-89665.herokuapp.com/', place_name)