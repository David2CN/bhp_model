from pathlib import Path

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'pressure_model'
DESCRIPTION = "A package for predicting downhole pressure in oil wells."
URL = "https://github.com/David2CN/bhp_model"
EMAIL = "onyealidavidcn@gmail.com"
AUTHOR = "David Onyeali"
REQUIRES_PYTHON = ">=3.6.0"

# about
about = {}
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / 'pressure_model'
with open(PACKAGE_DIR / "VERSION") as f:
    _version = f.read().strip()
    about["__version__"] = _version


# requirements
def list_reqs(fname="requirements.txt"):
    with open(ROOT_DIR / fname) as fd:
        return fd.read().splitlines()


setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    package_data={"pressure_model": ["VERSION"]},
    install_requires=list_reqs(),
    include_package_data=True,
    license="BSD-3",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)



