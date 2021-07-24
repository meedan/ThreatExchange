swig -c++ -python tmkpy.i
g++ -I../.. -O2 -fPIC -c tmkpy.cpp -L../cpp/ -ltmk
g++ -I../.. -O2 -fPIC -c tmkpy_wrap.cxx `python3-config --cflags` -L../cpp/ -ltmk
g++ -shared tmkpy.o tmkpy_wrap.o ../cpp/libtmk.a -o _tmkpy.so

