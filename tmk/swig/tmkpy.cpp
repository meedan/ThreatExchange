/* File: tmkpy.cpp */

#include <iostream>
#include <tmk/cpp/hashing/filehasher.h>
#include <tmk/cpp/algo/tmkfv.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <memory>

#include <tmk/swig/tmkpy.h>

using namespace std;
using namespace facebook::tmk;
using namespace facebook::tmk::algo;



facebook::tmk::algo::TMKFeatureVectors hashVideo(std::string inputVideoFileName, std::string ffmpegPath) {
  int resampleFramesPerSecond = 15; // TMK default
  std::string frameFeatureAlgorithmName = "pdqf";

  bool verbose = false;
  //std::string ffmpegPath = "/usr/local/bin/ffmpeg";
  //std::string inputVideoFileName = "";
  //std::string outputFeatureVectorsFileName = "";
  //std::string outputDirectory = "output/";

  facebook::tmk::algo::TMKFeatureVectors tmkFeatureVectors;

  facebook::tmk::io::TMKFramewiseAlgorithm tmkFramewiseAlgorithm =
    facebook::tmk::io::algoFromLowercaseName(frameFeatureAlgorithmName);
  if (tmkFramewiseAlgorithm == facebook::tmk::io::TMKFramewiseAlgorithm::UNRECOGNIZED) {
    fprintf(stderr, "%s: unrecognized algorithm name.\n", "pytmk");
    return tmkFeatureVectors; //Should be null
  }


  bool rc = facebook::tmk::hashing::hashVideoFile(
      inputVideoFileName,
      tmkFramewiseAlgorithm,
      ffmpegPath,
      resampleFramesPerSecond,
      tmkFeatureVectors,
      verbose,
      "pytmk");
  
  return tmkFeatureVectors;

}


facebook::tmk::algo::TMKFeatureVectors createTMKFeatureVectors(
      int framesPerSecond, // provenance
      int frameFeatureCount, // informational
      const facebook::tmk::algo::Periods& periods,
      const facebook::tmk::algo::FourierCoefficients& fourierCoefficients,
      const facebook::tmk::algo::FrameFeature& pureAverageFeature,
      const facebook::tmk::algo::FeaturesByPeriodsAndFourierCoefficients& cosFeatures,
      const facebook::tmk::algo::FeaturesByPeriodsAndFourierCoefficients& sinFeatures) {
  int resampleFramesPerSecond = 15; // TMK default
  std::string frameFeatureAlgorithmName = "pdqf";

  bool verbose = false;

  facebook::tmk::algo::TMKFeatureVectors tmkFeatureVectors; //std::shared_ptr

  facebook::tmk::io::TMKFramewiseAlgorithm tmkFramewiseAlgorithm =
    facebook::tmk::io::algoFromLowercaseName(frameFeatureAlgorithmName);

  tmkFeatureVectors=*(facebook::tmk::algo::TMKFeatureVectors::tryCreateFromPrecomputed(
      tmkFramewiseAlgorithm, // provenance
      framesPerSecond, // provenance
      frameFeatureCount, // informational
      periods,
      fourierCoefficients,
      pureAverageFeature,
      cosFeatures,
      sinFeatures));


  return tmkFeatureVectors;
}

/*//Default to 1 thread if not given
vector<float> query(TMKFeatureVectors needle, vector<string> haystackFilenames) {
	return query(needle,haystackFilenames,1);
}
*/

//Version with possibly more than one thread
vector<float> query(TMKFeatureVectors needle, vector<string> haystackFilenames, int numThreads) {

	//initalize return vector with -1's that is the same lenth as haystackFilenames
	vector<float> level2scores(haystackFilenames.size(), -1);
	
	if (numThreads<=1) {
		_query_worker(needle,haystackFilenames,level2scores,0,haystackFilenames.size());
	} else {
		if (numThreads>haystackFilenames.size()) {
			numThreads=haystackFilenames.size(); //No larger than the haystack length
		}
		int numPerThread=haystackFilenames.size()/numThreads; //integer division
		int start,end;
		for (int i=0; i<numThreads; i++) {
			start=i*numPerThread;
			if (i+1==numThreads) {
				end=haystackFilenames.size();
			} else {
				end=(i+1)*numPerThread;
			}
			//TODO: This should be done in a new thread
			_query_worker(needle,haystackFilenames,level2scores,start, end);
		}
	}

	return level2scores;

}

void _query_worker(TMKFeatureVectors needle, vector<string> haystackFilenames, vector<float> &level2scores, int start, int end) {
	fprintf(stderr,"_query_worker: %i %i\n",start,end);
	std::shared_ptr<TMKFeatureVectors> vid2;
	for (int i=start; i<end; i++) {
		//fprintf(stderr,"_query_worker: %i %s\n",i,haystackFilenames[i].c_str());
		vid2=TMKFeatureVectors::readFromInputFile(haystackFilenames[i].c_str(),"tmkpy");
		if (vid2==nullptr) {
			fprintf(stderr, "tmkpy: failed to read \"%s\".\n", haystackFilenames[i].c_str());
			continue;
		}
		//Now have a valid TMKFeatureVector. Compute L2 score
		//fprintf(stderr,"l2score: %f\n",TMKFeatureVectors::computeLevel2Score(needle,*vid2));
		level2scores[i]=TMKFeatureVectors::computeLevel2Score(needle,*vid2);
		
	}
}
