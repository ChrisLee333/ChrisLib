# setup.py

from setuptools import setup, find_packages

setup(
    name='ChrisLib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'qrcode',
        'setuptools',
        'pytube'
    ],
    description='Eine nützliche Python-Bibliothek namens ChrisLib',
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    author='Christoph Lederbogen',
    author_email='Christoph.Lederbogen@web.de',
    url='https://github.com/ChrisLee333/ChrisLib',
)
