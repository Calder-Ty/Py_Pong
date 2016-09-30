try:
    from setuptools import setup
except ImportError:
    from distutils import setup

config = {
    'description':'Impelementation of Pong in Python, for training and teaching OOP',

    'author': 'Tyler Calder',

    'url': '',

    'download_url' : '',

    'version' : '0.1',

    'install_requires' :['nose','sys'],

    'packages' : [],

    'scripts': [],

    'name': ''

    }

setup(**config)