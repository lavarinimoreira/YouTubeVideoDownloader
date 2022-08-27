# Import pythube library to download the video
import pytube

# Asking for the url video
url = input("Enter video url: ")

# We can teke the path as well, just uncomment the following line
# path = input("Enter path of storage")

# Specify the storage path of the video
path = "/home/gabriel/Videos"

# Magic line to download the video
pytube.YouTube(url).streams.get_highest_resolution().download(path)

