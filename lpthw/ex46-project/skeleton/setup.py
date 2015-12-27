try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My LPTHW ex46',
	'author': 'whocares',
	'url': 'somewhere on github',
	'author_email': 'none',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'LPTHW-ex46'
}

setup(**config)