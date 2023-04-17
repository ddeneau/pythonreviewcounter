from flask import Flask, jsonify
import googlemaps


app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'Number' : 32})


if __name__ == '__main__':
    app.run()

