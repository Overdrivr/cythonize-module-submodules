#!/usr/bin/env python
from setuptools import setup
from setuptools.extension import Extension
from distutils.dir_util import remove_tree
from pathlib import Path
import shutil
from glob import glob
import os

from Cython.Build import cythonize
from Cython.Distutils import build_ext

def cleanup_build_outputs():
    try:
        remove_tree('./build')
    except:
        pass

    try:
        remove_tree('./dist')
    except:
        pass

def scan_sources(root_dir):
    '''
    Scans the entire folder, retrieving all python files except
    __init__ files (see PROCESS.md step 1).
    '''
    scan_root = os.path.join(root_dir, '**.py')
    print('Scanning files in ', scan_root)
    files = glob(scan_root)
    files = [f for f in files if os.path.basename(f) != '__init__.py']
    print('Detected for compilation:', files)
    return files


# For removing build/dist folders (to have a clean build env everytime)
cleanup_build_outputs()

ext_modules = cythonize(scan_sources('mypkg'),
    build_dir="build",
    compiler_directives = {
        'always_allow_keywords': True
    }
)

setup(
    name='mypkg',
    version='0.1.0',
    description='Experiment compilation with Cython',
    author='Remi Beges',
    author_email='remi.beges@gmail.com',
    url='https://github.com/Overdrivr/cythonize-module-submodules/',
    packages=['mypkg'],
    ext_modules = ext_modules,
    cmdclass = {
        'build_ext': build_ext
    }
)
