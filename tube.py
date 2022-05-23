from pytube import YouTube

link = "https://www.youtube.com/watch?v=rV5qPKZa6_c"

yt = YouTube(link)

high =yt.streams.get_highest_resolution()
high.download("files")