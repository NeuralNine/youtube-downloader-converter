from moviepy.editor import VideoFileClip
import os
def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(filename[:-4] + ".mp3")
    os.remove(filename)
    clip.close()
