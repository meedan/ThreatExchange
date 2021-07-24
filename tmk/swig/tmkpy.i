/* File: tmkpy.i */
%module tmkpy
%include <std_string.i>
%{
#include <tmk/cpp/algo/tmkfv.h>
facebook::tmk::algo::TMKFeatureVectors hashVideo(std::string inputVideoFileName, std::string ffmpegPath);
%}

%import "std_vector.i"
%template() std::vector<float>;
%template() std::vector<int>;
%template() std::vector<std::vector<std::vector<float>>>;
%include <../cpp/algo/tmkfv.h>
facebook::tmk::algo::TMKFeatureVectors hashVideo(std::string inputVideoFileName, std::string ffmpegPath);
