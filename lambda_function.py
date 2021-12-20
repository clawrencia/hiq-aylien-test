from pipeline import fetch_stories
from pipeline import cron_db_methods
import time
import json
import logging
from datetime import datetime
from config import Config

def lambda_handler(event, context):

    #hardcode aylien params
    params = {
        "language" : ["en"],
        "published_at_start": "NOW-10MINUTES", # 16:53
        "per_page": 100
    }

    # Time everything for logging
    script_start = time.time()

    # --------------------------------------------------------
    #                  STORIES FROM AYLIEN
    # --------------------------------------------------------

    # This function gets the stories from the last 10 minutes from Aylien
    func_start = time.time()
    stories_dict = fetch_stories.fetch_stories(params, script_start)

    #This block inserts the Aylien stories to raw-stories        
    try:
        func_start = time.time()
        
        FILESIZE = 100
        N = max(int(len(stories_dict)/FILESIZE)+1,1)
        today = datetime.utcnow().date().strftime("%Y/%m/%d/")

        # Dump the stories in batches. This loop takes care of the remainder as well.
        for incre in range(N):
            file_name = datetime.utcnow().isoformat()
            full_path = today + file_name
            full_path = full_path.replace("%","").replace(".","").replace(":","-") + '.jsonl'

            batch = stories_dict[incre*FILESIZE:(incre+1)*FILESIZE]
            cron_db_methods.push_stories_to_s3(batch, full_path, 'holoniq-raw-stories-1')
        return {"statusCode": 200,"body": "Success"}
    
    except:
        return {
            "statusCode":502,"body": "Failed"
        }