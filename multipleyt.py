from pytube import YouTube

video_list = open("sample.txt","r")
for i in video_list:
    y = YouTube(i)
    try:
        dw = y.streams.get_by_itag(22)
        dw.download("F:/")
        print("DOWNLOADED ", i)
    except:
        dw = y.streams.first()
        dw.download("F:/")
        print("downloads", i)