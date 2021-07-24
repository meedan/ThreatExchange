/* File: tmkpy.i */
%module tmkpy
%include <std_string.i>
%{
#include <tmk/cpp/algo/tmkfv.h>
facebook::tmk::algo::TMKFeatureVectors hashVideo(std::string inputVideoFileName, std::string ffmpegPath);
facebook::tmk::algo::TMKFeatureVectors createTMKFeatureVectors(
      int framesPerSecond, // provenance
      int frameFeatureCount, // informational
      const facebook::tmk::algo::Periods& periods,
      const facebook::tmk::algo::FourierCoefficients& fourierCoefficients,
      const facebook::tmk::algo::FrameFeature& pureAverageFeature,
      const facebook::tmk::algo::FeaturesByPeriodsAndFourierCoefficients& cosFeatures,
      const facebook::tmk::algo::FeaturesByPeriodsAndFourierCoefficients& sinFeatures);
%}

%import "std_vector.i"
%template() std::vector<float>;
%template() std::vector<int>;
%template() std::vector<std::vector<std::vector<float>>>;
%include <../cpp/algo/tmkfv.h>
facebook::tmk::algo::TMKFeatureVectors hashVideo(std::string inputVideoFileName, std::string ffmpegPath);
facebook::tmk::algo::TMKFeatureVectors createTMKFeatureVectors(
      int framesPerSecond, // provenance
      int frameFeatureCount, // informational
      const facebook::tmk::algo::Periods& periods,
      const facebook::tmk::algo::FourierCoefficients& fourierCoefficients,
      const facebook::tmk::algo::FrameFeature& pureAverageFeature,
      const facebook::tmk::algo::FeaturesByPeriodsAndFourierCoefficients& cosFeatures,
      const facebook::tmk::algo::FeaturesByPeriodsAndFourierCoefficients& sinFeatures);
