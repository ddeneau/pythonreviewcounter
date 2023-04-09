from flask import Flask

app = Flask(__name__)

@app.route('/')
def count_reviews():
    return "32"


if __name__ == '__main__':
    app.run()

