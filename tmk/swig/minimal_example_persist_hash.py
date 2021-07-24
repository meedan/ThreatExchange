import tmkpy

#Compute hash
vid=tmkpy.hashVideo("../sample-videos/chair-19-sd-bar.mp4","/usr/bin/ffmpeg")

#Get the details
framesPerSecond=vid.getFramesPerSecond()
frameFeatureCount=vid.getFrameFeatureCount()
periods=vid.getPeriods()
fourierCoefficients=vid.getFourierCoefficients()
pureAverageFeature=vid.getPureAverageFeature()
cosFeatures=vid.getCosFeatures()
sinFeatures=vid.getSinFeatures()


#Create a new hash from the details
vid2=tmkpy.createTMKFeatureVectors(framesPerSecond,frameFeatureCount,periods,fourierCoefficients,pureAverageFeature,cosFeatures,sinFeatures)

#Compute level-1 and level-2 hashes between original and  recreated objects. 
level1=tmkpy.TMKFeatureVectors_computeLevel1Score(vid,vid2)
level2=tmkpy.TMKFeatureVectors_computeLevel2Score(vid,vid2)

#Score should be ~1.0
print(level1)
print(level2)

