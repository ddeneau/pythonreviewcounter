#import googlemaps
from flask import Flask, jsonify
#import requests
from datetime import datetime

app = Flask(__name__)

""" def count_reviews_alt():
    # Replace key='[insert your key without brackets]'
    google_maps_client = googlemaps.Client(key='AIzaSyDDKS_pV3ihaftl-2JRVEpqMlOZe8I0yp4')
    # Specify the place ID of the business
    place_id = 'ChIJ-Y7WtKnrToYRnPvOPI0dwJI'
    # Get the place details, including the number of reviews and name.
    review_count = \
        google_maps_client.place(place_id,
                                 fields=['user_ratings_total'])['result']['user_ratings_total']
    place_name = google_maps_client.place(place_id, fields=['name'])['result']['name']

    print(place_name + " Number of Reviews: " + str(review_count))

    return jsonify({place_name + "reviews": str(review_count)}) """

@app.route('/')
def count_reviews():
    return jsonify({"Number": "32"})


if __name__ == '__main__':
    app.run()

