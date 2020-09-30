from pytube import YouTube

yt= YouTube("Video URL you want to download")
dw = yt.streams.get_by_itag(22)
dw.download("F:/")

