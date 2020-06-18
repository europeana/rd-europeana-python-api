from setuptools import setup

setup(
    name='europeana',
    version='0.0.1',
    author='Jose Eduardo Cejudo',
    url = 'https://github.com/joseed-europeana/EuropeanaAPI.git',
    author_email='joseed.cejudo@europeana.eu',
    packages=['europeana'],
    include_package_data=True,
    install_requires=[
        #'schema==0.7.2',
        #'requests==2.23.0'
    ],
    entry_points={'console_scripts': ['main=europeana.main:main']})