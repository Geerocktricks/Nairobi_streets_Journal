from app import app
import urllib.request,json
from .models import articles , sources


Sources = sources.Sources
Articles = articles.Articles

api_key = app.config['NEWS_API_KEY']
base_url = app.config["SOURCES_URL"]
article_url = app.config["NEWS_API_BASE_URL"]

#*************************************Making first API Call for sources

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)
    # print(get_sources_url)

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