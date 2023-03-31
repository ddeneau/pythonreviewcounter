import googlemaps
from flask import Flask, jsonify
import requests
from datetime import datetime

app = Flask(__name__)


@app.route('/count_reviews')
def count_reviews():
    counter = 0
    # Replace key='[insert your key without brackets]'
    google_maps_client = googlemaps.Client(key='AIzaSyDDKS_pV3ihaftl-2JRVEpqMlOZe8I0yp4')
    # Specify the place ID of the business
    place_id = 'ChIJ7fLdskyTToYR81Dj4KgYsds'
    # Get the place details, including the reviews
    place_details = google_maps_client.place(place_id, fields=['reviews'])
    place_name = google_maps_client.place(place_id, fields=['name'])['result']['name']
    # Extract the reviews
    reviews = place_details['result']['reviews']

    # Print the reviews
    for review in reviews:
        counter = counter + 1
        print('Author:', review['author_name'])
        print('Rating:', review['rating'])
        print('Time:', datetime.fromtimestamp(review['time']))

    print(place_name + " Number of Reviews: " + str(counter))

    return jsonify({place_name + "reviews": str(counter)})


count_reviews()


if __name__ == '__main__':
    app.run()

