from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'


@app.route('/goodbye')
def hello_world():
    return 'Goodbye, Docker!'    
