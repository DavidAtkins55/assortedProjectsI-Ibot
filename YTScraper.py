# Import libraries
import os
import googleapiclient.discovery
from pytube import YouTube

api_key = os.environ.get("YOUTUBE_API_KEY")

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

# Get video statistics
request = youtube.videos().list(
    part="statistics",
    id="Ks-_Mh1QhMc"
)
response = request.execute()

print(response)


