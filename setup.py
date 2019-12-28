"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Flask Session Tutorial',
    version='0.0.1',
    description='Tutorial for interacting with Google Cloud Storage via the Python SDK.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hackersandslackers/googlecloud-storage-tutorial',
    author='Todd Birchard',
    author_email='todd@hackersandslackers.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='Google Cloud SDK Python Storage',
    packages=find_packages(),
    install_requires=['google-cloud-storage'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
        'env': ['python-dotenv']
    },
    entry_points={
        'console_scripts': [
            'install=main:__main__',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/hackersandslackers/googlecloud-storage-tutorial/issues',
        'Source': 'https://github.com/hackersandslackers/googlecloud-storage-tutorial/',
    },
)
