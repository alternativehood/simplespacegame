import os
from setuptools import setup, find_packages
import simplenamespace as module


def walker(base, *paths):
    file_list = set([])
    cur_dir = os.path.abspath(os.curdir)

    os.chdir(base)
    try:
        for path in paths:
            for dname, dirs, files in os.walk(path):
                for f in files:
                    file_list.add(os.path.join(dname, f))
    finally:
        os.chdir(cur_dir)
    return list(file_list)


requires = (
    'pyqt5',
)


setup(
    name=module.__name__.replace("_", "-"),
    version=module.__version__,
    author=module.__author__,
    description=module.package_info,
    platforms="all",
    classifiers=(
        'License :: Other',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Software Development',
    ),
    long_description=open('README.md').read(),
    packages=find_packages(exclude=('tests', 'tests.*')),
    package_data={
        module.__name__: walker(
            os.path.dirname(module.__file__)
        ),
    },
    install_requires=requires,
    extras_require={
        'develop': [
            'coverage!=4.3',
            'pylama',
            'pytest',
            'pytest-cov',
            'tox>=2.4',
        ],
    },
)
