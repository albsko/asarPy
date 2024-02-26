from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='asarPy',
    packages=['asarPy'],
    version='1.0',
    author='altsko',
    author_email='albertskonieczny@gmail.com',
    description='Library for working with .asar files',
    long_description=long_description,
    url='https://github.com/altsko/asarPy.git',
    keywords=['asar', 'electron', 'asarPy', 'pyasar'],
)
