import tmkpy
vid=tmkpy.hashVideo("../sample-videos/chair-19-sd-bar.mp4","/usr/bin/ffmpeg")
pure_avg=vid.getPureAverageFeature()
print(type(pure_avg),len(pure_avg))

cos_features=vid.getCosFeatures()
print(type(cos_features),len(cos_features[0][0]))

sin_features=vid.getSinFeatures()
print(type(sin_features),len(sin_features[0][0]))

