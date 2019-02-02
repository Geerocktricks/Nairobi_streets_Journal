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