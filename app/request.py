from app import app
import urllib.request,json
from .models import news_source,articles
Source = news_source.Source
Articles = articles.Articles



#Getting api key
api_key = '6edb7b566bad48f689bcc51c050f1db7'

#Getting the news base url
base_url = "https://newsapi.org/v2/sources?q={}&apiKey={}"
articles_base_url='https://newsapi.org/v2/everything?sources={}&apikey={}'
def get_sources(category):
    '''
    function that gets the json response to our url request
    '''
    news_source_url=base_url.format(category,api_key)

    with urllib.request.urlopen(news_source_url) as url:

        source_data = url.read()
        source_response = json.loads(source_data)
        source_results= None

        if source_response['sources']:
            source_results_list = source_response['sources']
            source_results = process_results(source_results_list)

        return source_results 


def process_results(source_list):
    '''
    Function that processes the news results and transform them to a list of objects
    '''
    source_results=[]

    for news_item in source_list:

        id=news_item.get('id')
        name=news_item.get('name')
        description=news_item.get('description')
        url=news_item.get('url')
        category=news_item.get('category')
        country=news_item.get('country')

           
        source_object = Source(id,name,description,url,category,country)
        source_results.append(source_object)


    return source_results   

def get_news_articles(id):
    '''
    Function that gets json response of articles for a specific source
    '''
    get_news_url=articles_base_url.format(id,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        news_data=url.read()
        news_response=json.loads(news_data)
        news_results= None

        if news_response['articles']:
            news_results_list=news_response['articles']
            news_results=process_articles_results(news_results_list)
    return news_results


def process_articles_results(news_updates):
    '''
    This function returns a list of new articles
    '''
    news_results = []
    for news_object in news_updates:
        id=news_object.get('id')
        name = news_object.get('name')
        author =  news_object.get('author')
        title = news_object.get('title')
        description = news_object.get('description')
        url = news_object.get('url')
        urlToImage =news_object.get('urlToImage')
        publishedAt = news_object.get('publishedAt')
        content = news_object.get('content')

        new_article = Articles(id,name,author,title,description,url,urlToImage,publishedAt,content)
        news_results.append(new_article)
    return news_results

