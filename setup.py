# -*- coding: utf-8 -*-

import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', 'Arguments to pass to tox')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        import shlex
        if self.tox_args:
            errno = tox.cmdline(args=shlex.split(self.tox_args))
        else:
            errno = tox.cmdline(self.test_args)
        sys.exit(errno)


def read_content(filepath):
    with open(filepath) as fobj:
        return fobj.read()


CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Customer Service',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Natural Language :: Portuguese',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities'
]

REQUIREMENTS = ['setuptools']

LONG_DESCRIPTION = '''
A Python wrapper for the Facebook Messenger API.

Read the documentation and learn how simple is to use it:
http://github.com/magrathealabs/mlabs-messenger
'''.strip()

setup(
    name='mlabs-messenger',
    description='A Python wrapper for the Facebook Messenger API',
    long_description=LONG_DESCRIPTION,
    keywords=['messenger', 'facebook', 'bot', 'bots', 'api'],
    version='0.1.0',
    packages=['messenger'],
    author='Magrathea Labs',
    author_email='contact@magrathealabs.com',
    url='http://www.magrathealabs.com',
    download_url='https://github.com/magrathealabs/mlabs-messenger/tarball/0.1.0',
    classifiers=CLASSIFIERS,
    data_files=[],
    install_requires=REQUIREMENTS,
    include_package_data=True,
    tests_require=['tox'],
    cmdclass={'test': Tox}
)
