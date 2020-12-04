from setuptools import setup
from Cython.Build import cythonize


# the setup file while will create the appropriate C objects
# side note, don't try to build a cython object with an existing __init__ file in the directory

setup(
    name='Factorial app',
    ext_modules=cythonize("factorial.pyx"),
    zip_safe=False,
)