#We import required packages
from moviepy.editor import *
import ffmpeg #ffmpeg-python needs to be installed for this to work
import os

##################################
#####This works using moviepy#####
##################################
#Video to Extract Audio from (Video B with Audio B according to the README.md)
mp4_file = "audio.mp4"
#Name of the Audio File to be created (Audio B according to the README.md)
mp3_file = "audio_final.mp3"
#Create VideoFileClip Object
videoclip = VideoFileClip(mp4_file)
#Create AudioClip using the audio of the mp4_file
audioclip = videoclip.audio
#We write an audio file with the audio of the mp4_file
audioclip.write_audiofile(mp3_file)


##################################
#####This works using FFMPEG######
##################################

print('Mixing Audio and video')
#We declare the Video we'll use (Video A with Audio A according to the README.md)
input_video = ffmpeg.input('video.mp4')
#We declare the Audio B extracted before
input_audio = ffmpeg.input('audio_final.mp3')
#We merge Video A with Audio B
ffmpeg.concat(input_video, input_audio, v=1, a=1).output('finalMergedVideo.mp4').run()

#We delete the extracted .mp3 file
os.remove("audio_final.mp3")
