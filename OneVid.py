import pytube
url = input("URL: ")
path = input("Path: ")
youtube = pytube.YouTube(url)
video = youtube.streams.get_by_itag(136)
video.download(path)
print ("done")
