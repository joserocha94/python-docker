from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/goodbye')
def goodbye_world():
    return 'Goodbye, Docker!'    

@app.route('/testing/')
def test_world():
    return 'This is a test, Docker!'    
