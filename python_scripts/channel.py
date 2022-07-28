#!/usr/bin/python

# This sample executes a search request for the specified search term.
# Sample usage:
#   python search.py --q=surfing --max-results=20
# NOTE: To use the sample, you must provide a developer key obtained
#       in the Google APIs Console. Search for "REPLACE_ME" in this code
#       to find the correct place to provide that key..

import argparse
import json
import numpy as np
import pprint
import csv

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.

DEVELOPER_KEY = 'AIzaSyDAptpTfh33KDwIuyVDB714gVVBe9yYIwE'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

    channels = {}
    
    i=0

    # this is a test script with a fixed Channel ID
    # For-loop is need by reading Channel IDs from a separate file, and make this call for all the IDs
    
    with open('../data_csv/channel_ids.csv', 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            search_response = youtube.channels().list(
                id=row,
                part='brandingSettings,contentDetails,contentOwnerDetails,id,localizations,snippet,statistics,status,topicDetails'
            ).execute()
            channels[i] = search_response.get('items',[i+1])[0]
            i = i+1    
    
    file_name = 'channels.json'
    import os
    file_path = 'channels.json'

    # check if size of file is 0
    with open(file_name, 'w') as f:
       json_object = json.dumps(channels, indent = 4)
       z = json.loads(json_object)
       json.dump(z, f, indent = 4)
    print(type(channels[1]))
    print('file dumped')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--q', help='Search term', default='ft.')
    parser.add_argument('--max-results', help='Max results', default=25)
    args = parser.parse_args()

try:
    youtube_search(args)
except HttpError as e:
    print ('An HTTP error %d occurred:\n%s') % (e.resp.status, e.content)