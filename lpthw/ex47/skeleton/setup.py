try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My roguelike (tutorial by roguebasin.com)',
	'author': 'roguebasin',
	'url': 'http://www.roguebasin.com/index.php?title=Complete_Roguelike_Tutorial,_using_python%2Blibtcod',
	'author_email': 'none',
	'install_requires': ['libtcodpy'],
	'packages': ['rl'],
	'scripts': [],
	'name': 'LPTHW-ex46'
}

setup(**config)