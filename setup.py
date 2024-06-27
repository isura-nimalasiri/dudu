# setup.py

from setuptools import setup, find_packages

setup(
    name='dudu',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dudu=dudu.main:main',
        ],
    },
    install_requires=[],
    description='A package to find common elements in a list and print counts of each element and the number of occurrences',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/dudu',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
