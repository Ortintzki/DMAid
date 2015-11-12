"""
Setup file for DMAid
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

CONFIG = {
            'description': 'A dungeons and dragons platform for creating new characters and playing on a grid.',
            'author': 'Jonas "Ortin" Tarnowetzki',
            'url': 'www.github.com/ortintzki/dmaid',
            'download_url': 'www.github.com/ortintzki/dmaid',
            'author_email': 'ortintzki@gmail.com',
            'version': '0.1.0',
            'install_requires': [],
            'packages': ['dmaid'],
            'scripts': [],
            'name': 'DMAid',
         }
setup(**CONFIG)

# 'Flask', 'Flask-RESTful', 'Flask-pymongo', 'itsdangerous', 'Jinja2', 'MarkupSafe', 'nose', 'mongodb', 'wxpython'