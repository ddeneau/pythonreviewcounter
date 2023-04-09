from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def __main__():
    return jsonify({
        'hello': 'world'
    })


if __name__ == '__main__':
    app.run()

