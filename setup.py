from distutils.core import setup
import symfind

setup(
    name='symfind',
    version=symfind.__version__,
    description='Find out which linked libs undefined symbols live in',
    long_description=open('README.rst').read(),
    author='Anton Backer',
    author_email='olegov@gmail.com',
    url='http://www.github.com/staticshock/symfind',
    license='ISC',
    entry_points={
        'console_scripts': [
            'symfind = symfind:main',
        ],
    },
    py_modules=['symfind'])
