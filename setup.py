import os
from pathlib import Path
from setuptools import setup, find_packages
from Cython.Build import cythonize

if not Path('./build').is_dir():
    os.mkdir("build")

setup(
    name='cython-vs-pypy-performance',
    version='0.1.0',
    license='MIT',

    ext_modules=cythonize("perf/*.pyx",
            build_dir="build"),

    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Topic :: Education :: Testing",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
