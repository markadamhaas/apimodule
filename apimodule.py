
from googleapiclient.discovery import build

api_key = 'AIzaSyCgsRFnlbyoWizsJ0xPDr06AEz8mtH81MI'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
		part='statistics, brandingSettings',
		id='UC9qkQ1s5iWY6PzYZ5BiD-tQ'
	)

response = request.execute()

channelName = response.get('items')[0].get('brandingSettings').get('channel').get('title')

description = response.get('items')[0].get('brandingSettings').get('channel').get('description')

viewCount = response.get('items')[0].get('statistics').get('viewCount')

subCount = response.get('items')[0].get('statistics').get('subscriberCount')

vidCount = response.get('items')[0].get('statistics').get('videoCount')

print('Channel:', channelName)
print('Description:', description)
print('Subsribers:', subCount)
print('Videos:', vidCount)
print('Views:', viewCount)