from setuptools import setup, find_packages
import os
from pathlib import Path

# create a list so that you don't have to type requirements.txt manually
root_path = os.path.dirname(os.path.realpath(__file__))
root_path = Path(root_path)

with open(root_path.joinpath('requirements.txt')) as f:
    install_requires = f.read().splitlines()

setup(
    name='pyeuropeana',
    version='0.1.0',
    install_requires = install_requires,
    package_dir={"": "src"},
    packages=find_packages(where="src")
)