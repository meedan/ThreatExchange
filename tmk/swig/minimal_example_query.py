import tmkpy
import glob
vid=tmkpy.hashVideo("../sample-videos/chair-19-sd-bar.mp4","/usr/bin/ffmpeg")

haystack=[f for f in glob.glob("../sample-hashes/*.tmk")]

scores=tmkpy.query(vid,haystack,1)

scores=[(x,y) for x,y in zip(haystack,scores)]
print(scores)

