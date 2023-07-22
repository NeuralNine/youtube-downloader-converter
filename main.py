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

print("Welcome to NeuralNine YouTube Downloader and Converter v0.3\n")
print("Loading modules...")

from youtube_downloader import download_playlist,input_links,download_video,convert_to_mp3
import os

print("Load Complete\n")
print('''
Options

(1) Download YouTube Videos Manually
(2) Download a YouTube Playlist
(3) Download YouTube Videos and Convert Into MP3

Downloading copyrighted YouTube videos is illegal!
We are not responsible for your downloads! Go at your own risk!

Copyright - Free Use license\n
''')

#Asks user for choice
choice = input("Choice: ")

if choice == "1" or choice == "2":

    # Sets Quality Option of video(s)
    quality = input("Please choose a quality (low or 0, medium or 1, high or 2, very high or 3):")

    if choice == "1": # Download YouTube Videos Manually
        links = input_links()
        print('Download has been started')
        for link in links: download_video(link, quality)
        print("Download finished!")

    if choice == "2": # Download a YouTube Playlist
        link = input("Enter the link to the playlist: ")
        print("Downloading playlist...")
        download_playlist(link, quality)
        print("Download finished!")

elif choice == "3": # Download YouTube Videos and Convert Into MP3
    links = input_links()
    for link in links:
        print("Downloading...")
        filename = download_video(link, 'low')
        print("Converting...")
        convert_to_mp3(filename)
        os.remove(filename)
else:
    # If input is anything other than 1,2 or 3. The program will exit.
    print("Invalid input! Terminating...")
    exit()