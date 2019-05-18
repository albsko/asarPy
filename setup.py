from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='asarPy',
    packages=['asarPy'],
    version='1.0',
    author='AS1337',
    author_email='as1337@gmail.com',
    description='Library for working with .asar files',
    long_description=long_description,
    url='https://github.com/AS1337/asarPy.git',
    keywords=['asar', 'electron', 'asarPy', 'pyasar'],
)
