from flask import render_template #import the render_template function from Flask
from app import app #import the app instance from flask



#views 
@app.route('/')
def index():
    '''
    Root page function that returns the index page
    '''
    return render_template('index.html')


