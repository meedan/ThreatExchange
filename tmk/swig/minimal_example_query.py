import tmkpy
import glob
from datetime import datetime
import random

vid=tmkpy.hashVideo("../sample-videos/chair-19-sd-bar.mp4","/usr/bin/ffmpeg")

haystack=[f for f in glob.glob("../sample-hashes/*.tmk")]
#haystack=[item for item in haystack for i in range(50)] #Make the list 50 copies every file
#random.shuffle(haystack)


start=datetime.now()
scores=None
try:
	scores=tmkpy.query(vid,haystack,1)
except RuntimeError as e:
	print(e)

end=datetime.now()

print(end-start)

if scores!=None:
	for file,score in zip(haystack,scores):
		print(file,score)

