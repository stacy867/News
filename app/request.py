from app import app
import urllib.request,json
from .models import source
from .models import article

Source = source.Source
Article = article.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the source and article base url
article_url = app.config['NEWS_ARTICLE_BASE_URL']
source_url =app.config['NEWS_SOURCE_BASE_URL']


def get_source(category):
    '''
    function that gets the json response to our url request
    '''
    get_source_url = source_url.format(category,api_key)
    print(get_source_url)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        

        source_result = None

        if get_source_response['sources']:
            source_result_list = get_source_response['sources']
            source_result = process_sourceresults(source_result_list)
    
    return source_result

def process_sourceresults(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_result: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        country = source_item.get('country')
        sourceurl = source_item.get('url')
        

        if sourceurl:
            source_object = Source(id,name,country,sourceurl)
            source_results.append(source_object)

    return source_results


def get_article(id):
    '''
    function that gets the json response to our url request
    '''
    get_article_url = article_url.format(id,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_result = None

        if get_article_response['articles']:
            article_result_list = get_article_response['articles']
            article_result = process_articleresults(article_result_list)

    return article_result


def process_articleresults(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of source objects
    '''
    article_results = []
    for article_item in article_list:
        author = article_item.get('author')
        tittle = article_item.get('title ')
        imageurl = article_item.get('urlToImage')
        description = article_item.get('description')
        time = article_item.get('publishedAt')
        url = article_item.get('url')
        
        

        if imageurl:
            article_object = Article(author,tittle,imageurl,description,time)
            article_results.append(article_object)

    return article_results