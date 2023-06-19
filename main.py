from pytube import YouTube

link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

# Where to save
SAVE_PATH = r"C:\Users\pc1\Desktop\mainfolder\youtube"  # to_do: change the path according to your needs

# Quality of the video
stream = yt.streams.get_highest_resolution()

# Downloading the video
stream.download(SAVE_PATH)
print("Download completed!!")
