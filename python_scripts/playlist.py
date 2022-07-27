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
import os

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.

DEVELOPER_KEY = 'AIzaSyDAptpTfh33KDwIuyVDB714gVVBe9yYIwE'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def get_video_ids(youtube, playlist_id):

    request = youtube.playlistItems().list(
            part='id,contentDetails,snippet',
            playlistId = playlist_id,
            maxResults=50
        )
    response = request.execute()

    video_ids = []

    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])

    next_page_token = response.get('nextPageToken')
    more_pages = True

    while more_pages:
        if next_page_token is None:
            more_pages = False
        else:
            request = youtube.playlistItems().list(
                        part='id,contentDetails,snippet',
                        playlistId = playlist_id,
                        maxResults = 50,
                        pageToken = next_page_token)

            response = request.execute()

            for j in range(len(response['items'])):
                video_ids.append(response['items'][j]['contentDetails']['videoId'])

            next_page_token = response.get('nextPageToken')

    return video_ids

def get_video_details(youtube, video_ids):

    all_videos = []
    print("Number of Videos: " + str(len(video_ids)))

    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part='statistics,contentDetails,liveStreamingDetails,localizations,snippet,player,recordingDetails,snippet,status,topicDetails',
            id=','.join(video_ids[i:i+50]))
        response = request.execute()
        all_videos.append(response.get('items',[]))

    return all_videos

def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

    playlists = {}
    videos = {}

    # this is a test script with a fixed Channel ID
    # For-loop is need by reading Channel IDs from a separate file, and make this call for all the IDs
    
    with open('../data_csv/game_playlist_ids.csv', 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            print(row[0])
            playlists[row[0]] = get_video_ids(youtube, row[0])
            videos[row[0]] = get_video_details(youtube, playlists[row[0]])


    # check if size of file is 0
    with open('../data_csv/game_playlists.json', 'w') as f:
       json_object = json.dumps(playlists, indent = 4)
       z = json.loads(json_object)
       json.dump(z, f, indent = 4)
    print('Playlists dumped')

    with open('../data_csv/game_channel_videos.json', 'w') as f:
       json_object = json.dumps(videos, indent = 4)
       z = json.loads(json_object)
       json.dump(z, f, indent = 4)
    print('Videos dumped')




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--q', help='Search term', default='ft.')
    parser.add_argument('--max-results', help='Max results', default=25)
    args = parser.parse_args()

try:
    youtube_search(args)
except HttpError as e:
    print ('An HTTP error %d occurred:\n%s') % (e.resp.status, e.content)