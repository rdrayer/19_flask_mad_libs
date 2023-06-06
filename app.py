from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_route():
    return '''
    <h1>Home Page</h1>
    '''