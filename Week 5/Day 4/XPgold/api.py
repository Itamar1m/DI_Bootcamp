import requests
import json
from googleapiclient.discovery import build
api_key='AIzaSyDuG7Z-jW66BIIaD0BBLF3uesmv7aYJaTg'

youtube=build('youtube','v3',developerKey=api_key)

request=youtube.channels().list(part='statistics',forUsername='schafer5')

response =request.execute()
text=json.dumps(response,indent=2)
# print (text)
print(response['items'][0]['statistics']['viewCount'])