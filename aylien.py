import logging
import time
from pprint import pprint
import os 

import aylien_news_api
from aylien_news_api.rest import ApiException

from config import Config


_configuration = aylien_news_api.Configuration()
_configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = os.environ['AYLIEN_APP_ID']
_configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = os.environ['AYLIEN_APP_KEY']
_client = aylien_news_api.ApiClient(_configuration)
_api_instance = aylien_news_api.DefaultApi(_client)

def search_story(params={}):
    response = _api_instance.list_stories(title = params['title'], source_domain=params['source_domain'])
    stories = [s.to_dict() for s in response.stories]
    params['cursor'] = response.next_page_cursor
    return stories

def fetch_new_stories(params={}, limit_stories=99999):
    fetched_stories = []
    stories = None

    while stories is None or len(stories) > 0:
        try:
            response = _api_instance.list_stories(**params)
        except ApiException as e:
            _logger.exception(e)
            if e.status == 429:
                time.sleep(20)
                continue

        stories = response.stories
        params['cursor'] = response.next_page_cursor

        fetched_stories += stories
        if(len(fetched_stories) >= limit_stories):
            return fetched_stories[:limit_stories]

    return fetched_stories


def fetch_stories_generator(params={}):
    fetched_stories = []
    stories = None

    while stories is None or len(stories) > 0:
        try:
            response = _api_instance.list_stories(**params)
        except ApiException as e:
            if e.status == 429:
                time.sleep(20)
                continue

        stories = response.stories
        params['cursor'] = response.next_page_cursor

        yield stories


def fetch_clusters_generator(params={}):
    fetched_clusters = []
    clusters = None

    while clusters is None or len(clusters) > 0:
        try:
            response = _api_instance.list_clusters(**params)
           
        except ApiException as e:
            if e.status == 429:
                time.sleep(20)
                continue

        clusters = response.clusters
        params['cursor'] = response.next_page_cursor

        yield clusters
