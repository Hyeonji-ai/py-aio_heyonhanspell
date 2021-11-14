#!/usr/bin/env python
from setuptools import setup, find_packages

with open("README.md", "r",encoding="UTF-8") as fh:
    long_description = fh.read()
def install():
    required = []
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
        for req in requirements:
            p = req.split('==')
            required.append(p[0])
    setup(
        name='py-aiohanspell',
        version='1.1',
        description="비동기 한글 맞춤법검사 모듈입니다.",
        long_description=long_description,
        long_description_content_type="text/markdown",
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
        python_requires='>=3.7'
    )


if __name__ == "__main__":
    install()
