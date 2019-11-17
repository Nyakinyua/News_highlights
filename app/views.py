from flask import render_template #import the render_template function from Flask
from app import app #import the app instance from flask
from .request import get_sources


#views 
@app.route('/')
def index():
    '''
    Root page function that returns the index page
    '''

    #Getting news sources
    various_sources=get_sources('category')
    

    title='Catch up on the latest news as and when they happen. keep i here for more information'
    message='whatever I write now can\t e blammed on me'

  
    return render_template('index.html', message=message,title=title, sources=various_sources)


@app.route('/source/<source_id>')
def source(source_id):

    return render_template('source.html',id=source_id)




