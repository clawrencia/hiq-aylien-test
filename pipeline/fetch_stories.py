import time
import sys
import os
import aylien_news_api
import requests
from datetime import datetime, date
from urllib.parse import urlparse

from libs import aylien
from config import Config

from nanoid import generate


LIMIT_STORIES = 10


def fetch_stories(params,script_start):

    # Get stories from Aylien
    print('Begin to fetch aylien story batch {}'.format(Config.AYLIEN_BATCH_NUMBER))
    
    #limit stories 2nd param for testing
    stories = aylien.fetch_new_stories(params, limit_stories=LIMIT_STORIES)

    # Transform story objects to dictionaries for the ease of processing
    stories_dict = [s.to_dict() for s in stories] 
    print('Finished getting {} stories in {:.2f}s'.format(len(stories), time.time() - script_start))

    return stories_dict
