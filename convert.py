import moviepy.editor as mp
import os
print("FUCK OFF SPACE")
music = []
folder = os.path.abspath(os.curdir)
for folder, subfolders, files in os.walk(folder):
	for file in files:
		if file.endswith(".mp4"):
			music.append(file)
iterat = 0
count = len(music)
print(music)
for iterat in range(0, count):
	music[iterat]=music[iterat][:-4]
print(music)

for iterat in range(0, count):
	clip = mp.VideoFileClip(music[iterat]+".mp4")
	clip.audio.write_audiofile(music[iterat]+".mp3")
