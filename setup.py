#!/usr/bin/env python3

'''
setup.py

Setup configuration file for the launch-library-api package.
'''


_SHORT_DESCRIPTION = 'A simple wrapper for the Launch Library API.'


def _readme():
    readme_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(readme_dir, 'README.md')) as readme:
            return readme.read()
    except IOError as e:
        return None


setup(
    name='launch-library-api',
    version='0.0',
    description=_SHORT_DESCRIPTION,
    long_description=_readme(),
    author='moge233',
    license='GNU',
    packages=find_packages(),
    zip_safe=False,
)
