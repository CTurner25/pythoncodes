from pytube import YouTube
from sys import argv

link = argv[1]
print(link)
yt = YouTube(link)
   
print("Title:", yt.title)
print("Views:", yt.views)

# Get the highest resolution stream
yd = yt.streams.get_highest_resolution()
    
# Download the video to the current directory
yd.download("C:/Users/Christopher Turner/Videos/Youtube")
    
# terminal- python 3 Youtube downloader.py “ link”
print(link)