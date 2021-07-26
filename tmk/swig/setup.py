#!/usr/bin/env python
"""
import setuptools.command.build_py


class BuildPyCommand(setuptools.command.build_py.build_py):
	#Custom build command.

	def run(self):
		self.run_command('pylint')
		setuptools.command.build_py.build_py.run(self)


setuptools.setup(
	cmdclass={
		'pylint': PylintCommand,
		'build_py': BuildPyCommand,
	},
	# Usual setup() args.
	# ...
)
"""

from distutils.core import setup, Extension



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
)
