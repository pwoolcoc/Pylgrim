try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

config = {
        'description': '',
        'author': 'Paul Woolcock',
        'author_email': 'pwoolcoc@gmail.com',
        'version': '0.1',
        'install_requires': [],
        'packages': find_packages(),
        'name': 'Pilgrim',
        'test_suite': 'nose.collector',
        'tests_require': ['nose'],
}

setup(**config)

