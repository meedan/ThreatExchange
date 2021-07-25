/* File: tmkpy.i */
%module tmkpy
%include <std_string.i>
%{
#include <tmk/cpp/algo/tmkfv.h>
#include <tmk/swig/tmkpy.h>
%}

%import "std_vector.i"
%template() std::vector<float>;
%template() std::vector<int>;
%template() std::vector<std::vector<std::vector<float>>>;
%template() std::vector<std::string>;
%include <../cpp/algo/tmkfv.h>
%include <../cpp/io/tmkiotypes.h>
%include <tmkpy.h>
