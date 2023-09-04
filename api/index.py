from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """
    This function handles the home page route.
    
    :return: HTML string for the home page.
    """
    return '<h1>Hello, World!</h1>'

@app.route('/about')
def about():
    """
    This function handles the about page route.
    
    :return: HTML string for the about page.
    """
    return '<h1>About</h1>'