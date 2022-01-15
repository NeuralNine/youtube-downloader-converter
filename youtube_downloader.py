import pytube, os
from tqdm import tqdm
from itertools import cycle
from concurrent.futures import ThreadPoolExecutor

if not os.path.exists('downloaded'):
    os.makedirs('downloaded')

def download_video(url, resolution):
    itag = choose_resolution(resolution)
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(itag)
    stream.download(output_path='downloaded')
    return stream.default_filename

def download_videos(urls, resolution):
    
#     for url in tqdm(urls):
#         download_video(url, resolution)
        
    all_urls = urls
    resolutions = cycle([resolution])
    
    with ThreadPoolExecutor() as ex:
        list(tqdm(ex.map(download_video, all_urls, resolutions), total=len(all_urls)))
    

def download_playlist(url, resolution):
    playlist = pytube.Playlist(url)
    download_videos(playlist.video_urls, resolution)

def choose_resolution(resolution):
    if resolution in ["low", "360", "360p"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd"]:
        itag = 22
    elif resolution in ["high", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
        itag = 137
    elif resolution in ["very high", "2160", "2160p", "4K", "4k"]:
        itag = 313
    else:
        itag = 18
    return itag


def input_links():
    print("Enter the links of the videos (end by entering 'STOP'):")

    links = []
    link = ""

    while link != "STOP" and link != "stop":
        link = input()
        links.append(link)

    links.pop()

    return links
