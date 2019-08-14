"""The setup and build script for the find_subsequence utility."""

from setuptools import setup

def requirements():
    """Build the requirements list for this project"""

    with open('requirements.txt') as requirements:
        return [ install.strip() for install in requirements ]

setup(
    name='find_subsequence',
    version='0.1',
    py_modules=['find_subsequence'],
    install_requires=requirements(),
    author="Wallace Reis",
    author_email="wallace@reis.me",
    description="Utility to evaluate if a subsequence is interesting.",
    url="https://github.com/wreis/find_subsequence",
    entry_points='''
        [console_scripts]
        find_subsequence=find_subsequence:find_subsequence
    ''',
)
