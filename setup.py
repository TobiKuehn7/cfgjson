from setuptools import setup, find_packages

setup(
    name='cfgjson',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        # add dependencies
    ],
    extras_require={
        'dev': [
            'pytest', # testing
            'flake8', # linting
            'black', # code formatting
            'twine', # PyPI upload
        ],
    },
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Tobias Kühn',
    author_email='',
    description='Python package for easy json config file handling',
    url='https://github.com/TobiKuehn7/cfgjson',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
)
