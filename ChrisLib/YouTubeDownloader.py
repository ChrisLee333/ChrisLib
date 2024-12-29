import os
from ChrisLib.helper.getOutputPath import getPath
from pytube import YouTube

def ytDownload(url, filename = "yt.mp4", stdOutput = True):
    yt = YouTube(url)

    downloader = yt.streams.get_highest_resolution()
    print("downloading...")

    if(stdOutput):
        filename = os.path.join(getPath(), filename)

    downloader.download(filename=filename)
    print("done!")