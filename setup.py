from setuptools import setup, find_packages
import os
from pathlib import Path

root_path = os.path.dirname(os.path.realpath(__file__))
root_path = Path(root_path)

with open(root_path.joinpath('requirements.txt')) as f:
    install_requires = f.read().splitlines()

setup(
    name='pyeuropeana',
    version='0.1.0',
    install_requires = install_requires,
    packages=find_packages(include=['pyeuropeana', 'pyeuropeana.*'])
)