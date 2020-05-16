'''
    Sphinxcontrib-lpblocks
    ~~~~~~~~~~~~~~~~~~~~~~

    Sphinx extension to support Literate Programming.
'''

from setuptools import setup, find_packages


import sphinxcontrib.lpblocks.__about__ as about
import sphinxcontrib.lpblocks.__version__ as version

with open('README.rst') as f:
    long_description = f.read()


setup(
    name='sphinxcontrib-lpblocks',
    version=version.__version__,
    url=about.__url__,
    download_url=about.__pypi__,
    license=about.__license__,
    author=about.__author__,
    author_email=about.__email__,
    description=about.__summary__,
    description_content_type='text/x-rst',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Sphinx', 'sphinx_rtd_theme'],
    namespace_packages=['sphinxcontrib'],
    test_suite='nose.collector',
    tests_require=['nose', 'mock'],
)
