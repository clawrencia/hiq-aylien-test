from datetime import datetime
import collections
import copy
import time
import asyncio
import sys
import simplejson as json
import csv
import logging
from datetime import datetime, date
from collections import OrderedDict

import psycopg2

import numpy as np
import pandas as pd

import boto3
from config import Config



def push_stories_to_s3(stories, filename, bucket):

    try:
        jsonl_dump = ''
        for s in stories:
            jsonl_dump += '{}\n'.format(json.dumps(s, default=datetime.isoformat))
        # ignore the last \n
        jsonl_dump = jsonl_dump[:-1]

        s3 = boto3.client('s3')
        s3.put_object(
            Body=jsonl_dump,
            Bucket=bucket,
            Key=filename
        )
        print("Saved stories to S3 " + bucket + " : " + filename + " : " + str(len(stories)) + " stories")
    except:
        print("Failed to save stories to S3 " + bucket + " : " + filename, exc_info=True)