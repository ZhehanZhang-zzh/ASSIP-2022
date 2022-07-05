#!/usr/bin/python

# This sample executes a search request for the specified search term.
# Sample usage:
#   python3 search.py --q=surfing --max-results=20
# NOTE: To use the sample, you must provide a developer key obtained
#       in the Google APIs Console. Search for "REPLACE_ME" in this code
#       to find the correct place to provide that key..

import argparse
import json
import numpy as np

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = 'AIzaSyC_Z_VCyF6j8nWrVEtgG2WmBW3tHOwyx9A'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=options.q,
        part='id,snippet',
        maxResults=options.max_results
    ).execute()

    videos = []
    stat_names = ['title', 'videoId', 'channelId', 'channelTitle', 'viewCount', 'likeCount', 'favorite count', 'commentCount']
    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append(search_result['snippet']['title'])
            videos.append(search_result['id']['videoId'])
            videos.append(search_result['snippet']['channelId'])
            videos.append(search_result['snippet']['channelTitle'])
            search_response3 = youtube.videos().list(
                id=search_result['id']['videoId'],
                part='statistics'
            ).execute()
            for search_result in search_response3.get('items',[]):
                try:
                    videos.append(search_result['statistics']['viewCount'])
                    break
                except:
                    videos.append("no data")
            for search_result in search_response3.get('items',[]):    
                try:
                    videos.append(search_result['statistics']['likeCount'])
                    break
                except:
                    videos.append("no data")
            for search_result in search_response3.get('items',[]):
                try:
                    videos.append(search_result['statistics']['favoriteCount'])
                    break
                except:
                    videos.append("no data")
            for search_result in search_response3.get('items',[]):
                try:
                    videos.append(search_result['statistics']['commentCount'])
                    break
                except:
                    videos.append("no data")

    for i in range(int((len(videos)/8))-1):
        stat_names.append('title')
        stat_names.append('videoId')
        stat_names.append('channelId')
        stat_names.append('channelTitle')
        stat_names.append('viewCount')
        stat_names.append('likeCount')
        stat_names.append('favoriteCount')
        stat_names.append('commentCount')
    
    stat_names = np.array_split(stat_names, int((len(videos)/8)))
    videos = np.array_split(videos, int((len(videos)/8)))
    res = {}
    res2 = {}
    for i in range(len(stat_names)):
        arr = stat_names[i]
        arr2 = videos[i]
        res2 = dict(zip(arr,arr2))
        res[i] = res2
        
    
    #res = dict(zip(stat_names, videos))
    print ("stat names length: " + str(len(stat_names)))
    print ("videos length: " + str(len(videos)))
    #print ("Resultant dictionary is : " +  str(res))
    
    
    file_name = 'game_playerUnknown’sBattleground(pubg)_videos.json'
    import os
    file_path = 'game_playerUnknown’sBattleground(pubg)_videos.json'
    # check if size of file is 0
    with open(file_name, 'w') as f:
       json_object = json.dumps(res, indent = 4)
       z = json.loads(json_object)
       json.dump(z, f, indent = 4)
    
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