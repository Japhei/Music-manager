from ShazamAPI import Shazam
import os

library = "Z:\\path to my music\\"

for root, dirs, files in os.walk(library):
	for file in files:
		mp3_file_content_to_recognize = open(root + "\\" +  file, 'rb').read()
		shazam = Shazam(mp3_file_content_to_recognize)
		recognize_generator = shazam.recognizeSong()
		print("analysing ", file ,"...")
		try:
			response = next(recognize_generator)[1]
			if len(response["matches"]) <= 0:
				print("ERROR: Not recognized!")
				continue
			songData = response["track"]
			title = songData["title"] + " - " + songData["subtitle"]
			print("renaming: ", title)
			os.rename(root + "\\" + file, root + "\\" + title + ".mp3")
		except:
			print("failed. dublicate?")
print("done!")