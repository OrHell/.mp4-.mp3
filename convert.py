import moviepy.editor as mp
import shutil
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
music_format = []
for iterat in range(0,count):
	music_format.append(music[iterat])

for iterat in range(0, count):
	music_format[iterat].replace(' ', '_')

for iterat in range(0, count):
	os.rename(music[iterat], music_format[iterat])


for iterat in range(0, count):
	music[iterat]=music_format[iterat][:-4]


for iterat in range(0, count):
	clip = mp.VideoFileClip(music[iterat]+".mp4")
	clip.audio.write_audiofile(music[iterat]+".mp3")
'''
				os.rename(file_name, list_list[i]+'.png')
				shutil.move(list_list[i]+'.png', "C:\\info\\order")
				'''
