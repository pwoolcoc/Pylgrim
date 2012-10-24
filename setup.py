try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

config = {
        'description': open("README.md").read(),
        'author': 'Paul Woolcock',
        'author_email': 'pwoolcoc@gmail.com',
        'version': open("VERSION").read(),
        'install_requires': open("requirements.txt").read().split(),
        'packages': find_packages(),
        'name': 'Pylgrim',
        'test_suite': 'nose.collector',
        'tests_require': ['nose'],
}

setup(**config)

