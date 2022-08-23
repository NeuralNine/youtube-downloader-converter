from pytube import YouTube, Playlist
from pytube.cli import on_progress
import os

def download_video(url, resolution):
    itag = choose_resolution(resolution)
    video = YouTube(url,on_progress_callback=on_progress)
    stream = video.streams.get_by_itag(itag)
    stream.download()
    return stream.default_filename

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
    print("Enter the links of the videos (end by entering 'STOP' or 0):")

    links = []
    link = ""

    while link != "0" and link.lower() != "stop":
        link = input("video_url: ")
        links.append(link)
    
    if len(links)==0:
        print("you dont input links")
        print("you dont input links")
        os.exit()

    links.pop()

    return links