# from app import app
import urllib.request,json
from .models import Articles , Sources

# Getting api key
api_key = None
# Getting the movie base url
base_url = None
# sources_api = None
article_url = None


def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['API_KEY']
    base_url = app.config["SOURCES_URL"]
    article_url = app.config["NEWS_API_BASE_URL"]
    headlines_api = app.config["HEADLINES_API"]
    sources_article_api  = app.config["SOURCES_ARTICLE_API"]

#*************************************Making first API Call for sources

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data =url.read()
        get_sources_response = json.loads(get_sources_data)
        print(get_sources_data)
        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

#******************************************Processing the results for sources

def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain source details
    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        

        if name:
            source_object = Sources(id,name,description)
            source_results.append(source_object)

    return source_results


#**********************************************Making second APi call for articles

def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = article_url.format(id,api_key)
    # print(get_articles_url)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data =url.read()
        get_articles_response = json.loads(get_articles_data)
        print(get_articles_response)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)

    return article_results 


#**************************************************Processing articles results

def process_articles(article_list):
    '''
    Function  that processes the source result and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain source details
    Returns :
        source_results: A list of source objects
    '''
    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        name = article_item.get('name')
        description = article_item.get('description')
        title = article_item.get('title')
        author = article_item.get('author')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

    
        article_object = Articles(id,name,description,title,author,url,urlToImage,publishedAt)
        article_results.append(article_object)

    return article_results