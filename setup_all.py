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

def search_files_recursively(root_dir, pattern):
    '''Searches files inside subdirectories, including root directory

    '''
    scan_root = os.path.join(root_dir, pattern)
    files = glob(scan_root)
    scan_root = os.path.join(root_dir, '**' , pattern)
    files += glob(scan_root)
    return files

def scan_sources(root_dir):
    '''
    Scans the entire folder, retrieving all python files except
    __init__ files (see PROCESS.md step 1).
    '''
    print('Scanning files in ', root_dir)
    files = search_files_recursively(root_dir, '*.py')

    # Remove __init__.py from compilation, otherwise link error
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

class MyBuildExt(build_ext):
    def run(self):
        super(MyBuildExt, self).run()

        root_dir = os.getcwd()
        build_dir = os.path.join(root_dir, self.build_lib)
        target_dir = build_dir if not self.inplace else root_dir

        # Identify all init.py
        scan_root = os.path.join(root_dir, 'mypkg')
        pattern = '__init__.py'
        print('Searching for __init__.py in ', scan_root)
        files = search_files_recursively(scan_root, pattern)

        for f in files:
            diff = os.path.commonpath([root_dir, f])
            diff = f.replace(diff, '')
            dest = target_dir + diff
            import pdb; pdb.set_trace()
            print('cp %s -> %s' % (f, dest))
            shutil.copyfile(f, dest)

setup(
    name='mypkg',
    version='0.1.0',
    description='Experiment compilation with Cython',
    author='Remi Beges',
    author_email='remi.beges@gmail.com',
    url='https://github.com/Overdrivr/cythonize-module-submodules/',
    packages=[],
    ext_modules = ext_modules,
    cmdclass = {
        'build_ext': MyBuildExt
    }
)
