from flask import Flask, jsonify
import googlemaps


app = Flask(__name__)

@app.route('/')
def index():
    json_to_return = jsonify({'Number' : 32 })
    try:
        # Replace key='[insert your key without brackets]'
        google_maps_client = googlemaps.Client(key='AIzaSyDDKS_pV3ihaftl-2JRVEpqMlOZe8I0yp5')
        # Specify the place ID of the business
        place_id = 'ChIJ-Y7WtKnrToYRnPvOPI0dwJI'
        # Get the place details, including the number of reviews and name.
        review_count = \
            google_maps_client.place(place_id,
                                    fields=['user_ratings_total'])['result']['user_ratings_total']
        place_name = google_maps_client.place(place_id, fields=['name'])['result']['name']

        json_to_return = jsonify({place_name + "reviews": str(review_count)})
        print(place_name + " Number of Reviews: " + str(review_count))
    except: googlemaps.exceptions.ApiError

    return json_to_return


if __name__ == '__main__':
    app.run()

