from app import app
import urllib.request,json
from .models import news

News = news.News

#Getting api key
api_key = app.config['f7fd95001a4d451d9bdbd52c83f61b27']

#getting the news base url
base_url = app.config["http://newsapi.org/v2/everything?q=bitcoin&from=2020-06-02&sortBy=publishedAt&apiKey=f7fd95001a4d451d9bdbd52c83f61b27"]


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url as url:
        get_news_data = url.read()
        get_news_response =json.loads(get_movies_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_movies_response['results']
            news_results = process_results(news_results_list)

        return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('original_title')
        url = news_item.get('url')
        image = news_item.get('image_path')
        

        if image:
            news_object = News(id,title,url,image)
            news_results.append(news_object)

    return news_results