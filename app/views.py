from flask import render_template
from app import app
from request import get_news

#views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting recent news
    recent_news= get_news('recent')
    print(recent_news)
    title = 'Home - Stay updated with the latest news!'

    return render_template('index.html', title = title,recent_news = recent_news)