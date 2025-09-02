from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__) # makes our app a flask app

@app.route('/')
@app.route('/index')
def index():
    return "Hello world!"

if __name__ == "__main__":
    serve(app, host="0.0.0.0",port=8000)