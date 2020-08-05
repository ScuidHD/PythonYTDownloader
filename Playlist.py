from pytube import Playlist
pl = Playlist(input("Playlist URL: "))
pl.download_all(input("Path: "))
