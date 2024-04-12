from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="asarPy",
    packages=["asarPy"],
    version="1.0",
    author="albski",
    author_email="albertskonieczny@gmail.com",
    description="Library for working with .asar files",
    long_description=long_description,
    url="https://github.com/albski/asarPy.git",
    keywords=["asar", "electron", "asarPy", "pyasar"],
)
