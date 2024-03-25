from flask import Flask
app = Flask(__name__)
cd py   
@app.route('/')
def hello_world():
    return 'Hello, Docker!'
