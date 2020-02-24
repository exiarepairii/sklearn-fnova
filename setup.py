from distutils.core import setup
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'hyanova',
    version = '1.0.3',
    keywords = ('anova', 'sklearn','hyperparameter','hyperparameter importance'),
    description = 'A pure python implementation of fuctional ANOVA algorithm.',
    license = 'MIT',
    install_requires = ['numpy', 'pandas', 'tqdm'],
    author = 'Su Qiao',
    author_email = 'qiaosu98@outlook.com',
    url = 'https://github.com/exiarepairii/hyanova',
    packages = find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    platforms = 'any',
    python_requires='>=3.6',
)
