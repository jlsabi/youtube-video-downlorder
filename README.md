# youtube-video-downlorder
The Python code example provided here is intended solely for educational purposes, and is to be used responsibly. It is designed to help understand how the pytube library in Python works and how to interact with video platforms programmatically. Please remember to always respect the rights of content creators.

This Python script uses the pytube library to download YouTube videos in their highest available resolution. The user inputs a YouTube link, and the video is downloaded to a specified location on their computer.

Before you can run the script, you'll need to have the pytube library installed. If you haven't installed it yet, you can do so with pip:
pip install pytube

This Python script initiates by importing the YouTube class from the pytube library. It then prompts the user to input the URL of a YouTube video they wish to download.

Upon receiving the user's input, it creates a YouTube object with the inputted URL. This object contains various information about the video, including its title, number of views, and available streams (different formats the video can be downloaded in).
