from setuptools import setup, Extension

tmkpy_module = Extension('_tmkpy',
	sources=["tmkpy.i","tmkpy.cpp"],
	swig_opts=["-c++"],
	include_dirs=["../.."],
	libraries=["tmk"],
	library_dirs=["../cpp/"],	
)


setup(name='tmkpy',
	version='0.1',
	description='Python bindings for the TMK video similarity library',
	author='Scott Hale',
	author_email='scott@meedan.com',
	url='https://github.com/meedan/ThreatExchange/tree/swig',
	ext_modules=[tmkpy_module],
	py_modules=["tmkpy"],
	setup_requires=['wheel'],
	package_data = {'': ['tmkpy.h']}  # needed for sdist
)
