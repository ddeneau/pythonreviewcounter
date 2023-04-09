from flask import Flask, jsonify
#from datetime import datetime
#import requests
#import googlemaps

app = Flask(__name__)

@app.route('/')
def count_reviews():
    return jsonify({"Number": "32"})


if __name__ == '__main__':
    app.run()

