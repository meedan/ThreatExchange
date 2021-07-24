import tmkpy
vid=tmkpy.hashVideo("../sample-videos/chair-19-sd-bar.mp4","/usr/bin/ffmpeg")
pure_avg=vid.getPureAverageFeature()
print(type(pure_avg),len(pure_avg))

cos_features=vid.getCosFeatures()
print(type(cos_features),len(cos_features[0][0]))

sin_features=vid.getSinFeatures()
print(type(sin_features),len(sin_features[0][0]))

vid2=tmkpy.hashVideo("../sample-videos/chair-22-sd-grey-bar.mp4","/usr/bin/ffmpeg")
level1=tmkpy.TMKFeatureVectors_computeLevel1Score(vid,vid2)
level2=tmkpy.TMKFeatureVectors_computeLevel2Score(vid,vid2)

print("level-1 score",level1)
print("level-2 score",level2)

