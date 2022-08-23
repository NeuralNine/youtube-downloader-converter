import youtube_downloader as yd
import file_converter as fc
import os

print("Welcome to NeuralNine YouTube Downloader and Converter v0.2 Alpha")
print("Loading...")

print('''
What do you want?

(1) Download YouTube Videos Manually
(2) Download a YouTube Playlist
(3) Download YouTube Videos and Convert Into MP3

Downloading copyrighted YouTube videos is illegal!
I am not responsible for your downloads! Go at your own risk!

Copyright (c) NeuralNine 2020
''')

choice = input("Choice: ")

if choice == "1" or choice == "2":
    quality = input("Please choose a quality (low or 0, medium or 1, high or 2, very high or 3):")
    if choice == "2":
        link = input("Enter the link to the playlist: ")
        print("Downloading playlist...")
        yd.download_playlist(link, quality)
        print("Download finished!")
    if choice == "1":
        links = yd.input_links()
        for link in links:
            yd.download_video(link, quality)
        print("Download finished!")
elif choice == "3":
    links = yd.input_links()
    for link in links:
        print("Downloading...")
        filename = yd.download_video(link, 'low')
        print("Converting...")
        fc.convert_to_mp3(filename)
        os.remove(filename)
else:
    print("Invalid input! Terminating...")
