import os

from setuptools import find_packages, setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


TESTS_REQUIRE = [
    'coverage',
    'nose',
]

setup(
    name="xamcheck.utils",
    version="0.0.1",
    author="Pankaj Singh",
    author_email="pankaj@policyinnovations.in",
    description=("Utility functions used in python projects of Xamcheck."),
    license = "BSD",
    keywords = "xamcheck utility",
    url = "http://packages.python.org/pypi/xamcheck.utils",
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['xamcheck'],
    extras_require=dict(
        test=TESTS_REQUIRE,
    ),
    install_requires=[
        'Django',
        'setuptools',
    ],
    tests_require=TESTS_REQUIRE,
    test_suite = 'nose.collector',
    include_package_data=True,
    zip_safe=False,
)
