from pytube import Playlist
playlist = Playlist("Playlist Link you want to download")
print('Number of videos in playlist: %s' % len(playlist.video_urls))
for video_url in playlist.video_urls:
    print(video_url)
playlist.download_all()

