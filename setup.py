# Standard Library
import os

# Third Party Stuff
from pip.req import parse_requirements
from setuptools import find_packages, setup
from setuptools.command.test import test as test_command

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements(
    os.path.join(os.path.dirname(__file__), 'requirements.txt',),
    session=0,
)

install_requires = [str(ir.req) for ir in install_reqs]


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


class NoseTestCommand(test_command):
    # Inspired by the example at https://pytest.org/latest/goodpractises.html

    def finalize_options(self):
        test_command.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # Run nose ensuring that argv simulates running nosetests directly
        import nose
        nose.run_exit(argv=['nosetests'])

TESTS_REQUIRE = [
    'coverage',
    'nose',
]


setup(
    name="xamcheck_utils",
    version="0.0.13",
    author="Pankaj Singh",
    author_email="pankaj@xamcheck.com",
    description=("Utility functions used in python projects of Xamcheck."),
    license="BSD",
    keywords="xamcheck utility",
    url="https://github.com/psjinx/xamcheck-utils",
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['xamcheck_utils'],
    extras_require=dict(
        test=TESTS_REQUIRE,
    ),
    install_requires=install_requires,
    cmdclass={'test': NoseTestCommand},
    tests_require=TESTS_REQUIRE,
    test_suite="nose.collector",
    include_package_data=True,
    zip_safe=False,
)
