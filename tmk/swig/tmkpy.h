//tmkpy.h

#include <tmk/cpp/algo/tmkfv.h>
#include <tmk/cpp/io/tmkio.h>

using namespace std;
using namespace facebook::tmk;
using namespace facebook::tmk::algo;

TMKFeatureVectors hashVideo(string inputVideoFileName, string ffmpegPath);
TMKFeatureVectors createTMKFeatureVectors(
      int framesPerSecond, // provenance
      int frameFeatureCount, // informational
      const Periods& periods,
      const FourierCoefficients& fourierCoefficients,
      const FrameFeature& pureAverageFeature,
      const FeaturesByPeriodsAndFourierCoefficients& cosFeatures,
      const FeaturesByPeriodsAndFourierCoefficients& sinFeatures);

//vector<float> query(TMKFeatureVectors needle, vector<string> haystackFilenames);
vector<float> query(TMKFeatureVectors needle, vector<string> haystackFilenames, int numThreads);
void _query_worker(TMKFeatureVectors needle, vector<string> haystackFilenames, vector<float> &level2scores, int start, int end);
