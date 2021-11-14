#!/usr/bin/env python
from setuptools import setup, find_packages


def install():
    required = []
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
        for req in requirements:
            p = req.split('==')
            required.append(p[0])
    desc = ''
    setup(
        name='py-aiohanspell',
        version='1.0',
        description=desc,
        long_description=desc,
        author='SpaceDEV',
        author_email='support@spacedev.space',
        url='https://github.com/spacedev-official/py-aiohanspell',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Education',
            'Intended Audience :: End Users/Desktop',
            'License :: Freeware',
            'Operating System :: POSIX',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: MacOS :: MacOS X',
            'Topic :: Education',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8'
        ],
        packages=find_packages(),
        install_requires=required,
    )


if __name__ == "__main__":
    install()
