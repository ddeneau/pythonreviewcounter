from flask import Flask, jsonify
import googlemaps

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def index():
    google_maps_client = googlemaps.Client(key='YOUR_KEY')
    place_id = 'ChIJ-Y7WtKnrToYRnPvOPI0dwJI'
    review_count = google_maps_client.place(place_id, fields=['user_ratings_total'])['result']['user_ratings_total']
    data = {"number" : review_count}
    return jsonify(data)


if __name__ == '__main__':
    print(googlemaps.__version__)
    app.run()

