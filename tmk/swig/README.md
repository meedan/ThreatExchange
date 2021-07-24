# SWIG Python Bindings

First build the TMK C++ code per the instructions at ../cpp/ . You may need to upodate the location of ffmpeg in Makefile

Ensure swig is installed and then build this extension with `./build.sh`

Check the location of ffmpeg in `minimal_example.py` and then run it. 
You should see a level1 score of 0.953346 and a level2 score of 0.962158


