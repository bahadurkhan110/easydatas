# setup.py
from setuptools import setup, find_packages

setup(
    name='easydatas',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'joblib',
    ],
)
