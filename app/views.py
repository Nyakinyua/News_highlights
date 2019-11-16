from flask import render_template #import the render_template function from Flask
from app import app #import the app instance from flask



#views 
@app.route('/')
def index():
    '''
    Root page function that returns the index page
    '''

    message='whatever I write now can\t e blammed on me'
    return render_template('index.html', title=message)


@app.route('/source/<source_id>')
def source(source_id):

    return render_template('source.html',id=source_id)



