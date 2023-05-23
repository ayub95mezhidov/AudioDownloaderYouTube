import pafy

url = 'Video URL'

video = pafy.new(url=url, ydl_opts={"ignoreerrors": True})
video._use_parser = False
video_title = video.title

for c in ['#', '|', '/', "\\"]:
    if c in video_title:
        video_title = video_title.replace(c, '')
filename = video_title + '.mp3'

best_audio = video.getbestaudio()
best_audio.download(filepath=filename)

print(video_title)

