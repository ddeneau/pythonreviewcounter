from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def count_reviews():
    return jsonify({"":""})


if __name__ == '__main__':
    app.run()

