/* File: tmkpy.cpp */

#include <iostream>
#include <tmk/cpp/hashing/filehasher.h>
#include <tmk/cpp/algo/tmkfv.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <memory>

using namespace std;

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


