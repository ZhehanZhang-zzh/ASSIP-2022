#!/usr/bin/python

# This sample executes a search request for the specified search term.
# Sample usage:
#   python search.py --q=surfing --max-results=10
# NOTE: To use the sample, you must provide a developer key obtained
#       in the Google APIs Console. Search for "REPLACE_ME" in this code
#       to find the correct place to provide that key..

import argparse
import json

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = 'YOUR_KEY'
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
    stat_names = ['title', 'videoId', 'channelId', 'channelTitle', 'viewCount', 'likeCount', 'favoriteCount', 'commentCount']
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
                videos.append(search_result['statistics']['viewCount'])
                videos.append(search_result['statistics']['likeCount'])
                videos.append(search_result['statistics']['favoriteCount'])
                videos.append(search_result['statistics']['commentCount'])
    for i in range(int((len(videos)/8))-1):
        stat_names.append('title' + str(i))
        stat_names.append('videoId' + str(i))
        stat_names.append('channelId' + str(i))
        stat_names.append('channelTitle' + str(i))
        stat_names.append('viewCount' + str(i))
        stat_names.append('likeCount' + str(i))
        stat_names.append('favoriteCount' + str(i))
        stat_names.append('commentCount' + str(i))

    
    res = dict(zip(stat_names, videos))
    print ("stat names length: " + str(len(stat_names)))
    print ("videos length: " + str(len(videos)))
    print(str(videos))
    print ("Resultant dictionary is : " +  str(res))
    
    
    file_name = 'videos.json'
    import os
    file_path = 'videos.json'
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