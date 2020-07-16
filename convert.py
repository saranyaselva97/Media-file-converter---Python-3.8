from moviepy.editor import *
mp4_file="socket vedo.avi"
mp3_file="audio.mp3"
VideoClip=VideoFileClip(mp4_file)
AudioClip= VideoClip.audio
AudioClip.write_audiofile(mp3_file)
AudioClip.close()
VideoClip.close()