from pytube import YouTube

url = input("https://www.youtube.com/watch?v=m_GoB8SFOeM&t=906s")

yt = YouTube(url)

stream = yt.streams.get_highest_resolution()

stream.download()
