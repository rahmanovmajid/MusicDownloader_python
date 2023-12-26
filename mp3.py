import youtube_dl

video_url=input("enter a link:")

video_name=youtube_dl.YoutubeDL().extract_info(url=video_url,download=False)
file_name=f"{video_name['title']}.mp3"

setting={
    'format':'bestaudio/best',
    'keepvideo':False,
    'outtmpl':file_name,
}


with youtube_dl.YoutubeDL(setting) as ydl:

 ydl.download([video_name['webpage_url']])


print(f"download has been completed {file_name}")