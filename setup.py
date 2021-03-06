#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    'Cython', 'h5py', 'numpy', 'scipy',
    'scikit-learn', 'pandas', 'pypandoc', 'pot', 'Flask',
    'gunicorn', 'numexpr', 'simplejson', 'psutil', 'scanpy'
]

extras_require = {
    'GRN': ["'gslrandom>=0.1'"],
}

setup_requirements = [
    # put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'unittest'
]

setuptools.setup(
    name='wot',
    version='0.1.5',
    description="Optimal transport for time-course single cell data",
    author="WOT Team",
    author_email='wot@broadinstitute.org',
    url='https://github.com/broadinstitute/wot',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(include=['wot']),
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='wot',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    python_requires='>= 3',
    entry_points={
        'console_scripts': [
            'wot=wot.__main__:main'
        ]
    }
)
