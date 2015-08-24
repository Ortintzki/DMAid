"""
Setup file for DnD_Platform
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

CONFIG = {
            'description': 'A dungeons and dragons platform for creating new characters and playing on a grid.',
            'author': 'Jonas "Ortin" Tarnowetzki',
            'url': 'www.github.com/ortintzki/dnd_platform',
            'download_url': 'www.github.com/ortintzki/dnd_platform',
            'author_email': 'ortintzki@gmail.com',
            'version': '0.1.0',
            'install_requires': ['nose', 'mongodb', 'wxpython'],
            'packages': ['dnd_platform'],
            'scripts': [],
            'name': 'DnD_platform',
         }
setup(**CONFIG)

