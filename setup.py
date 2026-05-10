from setuptools import setup, find_packages
import os
import re
import ast

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('flask_blogging/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))



BASE_PATH = os.path.dirname(__file__)


def get_requirements(suffix=''):
    with open(os.path.join(BASE_PATH, 'Requirements%s.txt' % suffix)) as f:
        rv = f.read().splitlines()
    return rv

setup(
    name='inkflow',
    version=version,
    url='https://github.com/jennica-z/inkflow',
    license='MIT',
    author='jennica-z',
    author_email='jennicazheng@hotmail.com',
    description='Lightweight personal writing system',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=get_requirements(),
    tests_require=["nose", "mysqlclient", "psycopg2"],
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
