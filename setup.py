#!/usr/bin/python
'''FANN Python bindings setup'''

import os
import os.path
import sys
import subprocess
from setuptools import setup, Extension, find_packages

NAME = 'fann2'
VERSION = '1.1.2'

with open("README.rst") as f:
    LONG_DESCRIPTION = f.read()

def find_executable(executable, path=None):
    '''Try to find 'executable' in the directories listed in 'path' (a
    string listing directories separated by 'os.pathsep'; defaults to
    os.environ['PATH']).'''
    if path is None:
        path = os.environ['PATH']
    paths = path.split(os.pathsep)
    extlist = ['']
    if os.name == 'os2':
        ext = os.path.splitext(executable)
        # executable files on OS/2 can have an arbitrary extension, but
        # .exe is automatically appended if no dot is present in the name
        if not ext:
            executable = executable + ".exe"
    elif sys.platform == 'win32':
        pathext = os.environ['PATHEXT'].lower().split(os.pathsep)
        ext = os.path.splitext(executable)
        if ext not in pathext:
            extlist = pathext
    for ext in extlist:
        execname = executable + ext
        if os.path.isfile(execname):
            return execname
        else:
            for pth in paths:
                fil = os.path.join(pth, execname)
                if os.path.isfile(fil):
                    return fil
            break
    else:
        return None

def find_x(path1):
    '''Return true if substring is in string for files
    in specified path'''
    libs = os.listdir(path1)
    for lib_dir in libs:
        if "doublefann" in lib_dir:
            return True

def find_fann():
    '''Find doublefann library'''
    # FANN possible libs directories (as $LD_LIBRARY_PATH), also includes
    # pkgsrc framework support.
    if sys.platform == "win32":
        dirs = sys.path
        for ver in dirs:
            if os.path.isdir(ver):
                if find_x(ver):
                    return True
        raise Exception("Couldn't find FANN source libs!")
    else:
        dirs = [os.environ.get('PREFIX','')+'/lib','/lib', '/usr/lib', '/usr/lib64', '/usr/local/lib', '/usr/pkg/lib']
        for path in dirs:
            if os.path.isdir(path):
                if find_x(path):
                    return True
        raise Exception("Couldn't find FANN source libs!")

def find_swig():
    '''Find SWIG executable path'''
    for executable in ("swig2.0", "swig"):
        if find_executable(executable):
            return executable
    raise Exception("Couldn't find SWIG binary!")

def build_swig():
    '''Run SWIG with specified parameters'''
    print("Looking for FANN libs...")
    find_fann()
    print("running SWIG...")
    swig_bin = find_swig()
    swig_cmd = [swig_bin, '-c++', '-python', 'fann2/fann2.i']
    subprocess.Popen(swig_cmd).wait()

if "sdist" not in sys.argv:
    build_swig()

setup(
    name=NAME,
    description='Fast Artificial Neural Network Library (FANN) Python bindings.',
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    author='Steffen Nissen',
    author_email='lukesky@diku.dk',
    maintainer='Gil Megidish, Vincenzo Di Massa and FutureLinkCorporation',
    maintainer_email='gil@megidish.net & hawk.it@tiscali,it and devel@futurelinkcorporation.com',
    url='https://github.com/FutureLinkCorporation/fann2',
    license='GNU LESSER GENERAL PUBLIC LICENSE (LGPL)',
    dependency_links=[
        "http://sourceforge.net/projects/fann/files/fann/2.2.0/FANN-2.2.0-Source.zip/download",
        "http://www.swig.org/download.html"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
    keywords="ANN artificial intelligence FANN2.2.0 bindings".split(' '),
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    py_modules=['fann2.libfann'],
    ext_modules=[Extension('fann2._libfann', ['fann2/fann2_wrap.cxx'],
                           include_dirs=['./include',
                                         '../include', 'include'],
                           libraries=['doublefann'],
                           define_macros=[("SWIG_COMPILE", None)]
                          ),
                ]
)
