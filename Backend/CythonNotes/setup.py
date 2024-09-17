# setup.py
from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Fibonacci',
    ext_modules=cythonize("fib.pyx", compiler_directives={'language_level' : "3"}),
)