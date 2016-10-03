try:
    from setuptools import setup
except ImportError:
    from distutils import setup

config = {
    'description':'Impelementation of Pong in Python, for training and teaching OOP/MVC',

    'author': 'Tyler Calder',

    'url': '',

    'download_url' : '',

    'version' : '0.1',

    'install_requires' :['unittest','sys', 'math', 'pygame', 'numpy'],

    'packages' : [],

    'scripts': [],

    'name': 'Py_Pong'

    }

setup(**config)