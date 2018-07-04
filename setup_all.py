#!/usr/bin/env python
from setuptools import setup
from setuptools.extension import Extension
from pathlib import Path
import shutil

from Cython.Build import cythonize
from Cython.Distutils import build_ext

ext_modules = cythonize([
    Extension("mypkg.*", ["mypkg/*.py"]),
    ],
    build_dir="build",
    compiler_directives = {
        'always_allow_keywords': True
    }
)

'''
class MyBuildExt(build_ext):
    def run(self):
        build_ext.run(self)

        build_dir = Path(self.build_lib)
        root_dir = Path(__file__).parent

        target_dir = build_dir if not self.inplace else root_dir

        self.copy_file(Path('mypkg') / '__init__.py', root_dir, target_dir)

    def copy_file(self, path, source_dir, destination_dir):
        if not (source_dir / path).exists():
            return

        shutil.copyfile(str(source_dir / path), str(destination_dir / path))
'''

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
