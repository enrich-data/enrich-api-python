# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages


setup(
    name='enrich-api',
    version='1.1.7',
    author=u'Valerian Saliou',
    author_email='valerian@valeriansaliou.name',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/enrich-data/enrich-api-python',
    license='MIT - http://opensource.org/licenses/mit-license.php',
    description='Enrich API Python.',
    long_description=open('README.md').read(),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
