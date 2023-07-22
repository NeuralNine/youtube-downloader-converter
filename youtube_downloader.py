#-------------------------------------------------------------------------------
# Name:         YouTube Downloader and Converter v0.3
#
# Author:       NeuralNine
#
# Created:      2020
# Copyright:    Free Use License
#
# Lead Dev :    NeuralNine
# Improvements: MT_276 [https://github.com/MT-276]
#               l20j45 [https://github.com/l20j45]
#               ProgrammingFire [https://github.com/ProgrammingFire]
#               aswnss-m [https://github.com/aswnss-m]
#-------------------------------------------------------------------------------

from pytube import YouTube, Playlist
from pytube.cli import on_progress
import os

def download_video(url, resolution):
    """
    Downloads video to a 'Downloaded' folder in the same dir as the program.
    """
    itag = choose_resolution(resolution)
    video = YouTube(url,on_progress_callback=on_progress)
    stream = video.streams.get_by_itag(itag)
    try:
        os.mkdir('./Downloaded/')
    except:
        pass
    stream.download(output_path='./Downloaded/')
    return f'./Downloaded/{stream.default_filename}'

def download_videos(urls, resolution):
    for url in urls:
        download_video(url, resolution)

def download_playlist(url, resolution):
    playlist = Playlist(url)
    download_videos(playlist.video_urls, resolution)

def choose_resolution(resolution):
    if resolution in ["low", "360", "360p","0"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd","1"]:
        itag = 22
    elif resolution in ["high", "1080", "1080p", "fullhd", "full_hd", "full hd","2"]:
        itag = 137
    elif resolution in ["very high", "2160", "2160p", "4K", "4k","3"]:
        itag = 313
    else:
        itag = 18
    return itag

def input_links():

    print("Enter the links of the videos (end by entering 'stop' or 0):")

    links = []
    link = ""

    while link != "0" and link.lower() != "stop":
        link = input("video_url: ")
        links.append(link)

    if len(links)==1:
        print("No links were inputed")
        exit()

    links.pop()

    return links

def convert_to_mp3(filename):
    from moviepy.editor import VideoFileClip

    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(filename[:-3] + "mp3")
    clip.close()
    os.remove(filename)