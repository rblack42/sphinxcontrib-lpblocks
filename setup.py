'''Sphinx lpblock domain

Domain to support Literate Programming.
'''
import io
import sys

from setuptools import setup, find_packages

def readfile(filename):
    with io.open(filename, encoding="utf-8") as stream:
        return stream.read().split("\n")

setup(
    name='sphinxcontrib-lpblocks',
    version=readfile('VERSION')[0].strip(),
    url='http://github.com/rblack42/sphinxcontrib-lpblocks',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-lpblocks',
    license='MIT',
    author='Roie R. Black',
    author_email='roie.black@gmail.com',
    description='Sphinx lpblocks extension',
    long_description=readfile('README.rst')[5:],
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Sphinx<1.6'],
    namespace_packages=['sphinxcontrib'],
    test_suite='nose.collector',
    tests_require=['nose', 'mock'],
)
