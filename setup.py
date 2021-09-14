from setuptools import setup, find_packages
from codecs import open

# Get the version in a safe way which does not refrence hatchet-vis `__init__` file
# per python docs: https://packaging.python.org/guides/single-sourcing-package-version/
version = {}
with open("./version.py") as fp:
    exec(fp.read(), version)

from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name="hatchet_vis",
    version=version["__version__"],
    description="Notebook-based VIS library for supporting analysis of hierarchical performance data in Hatchet.",
    url="https://github.com/jarusified/hatchet-vis-demo",
    author="",
    author_email="",
    license="MIT",
    classifiers=[ 
        "License :: OSI Approved :: MIT License",
    ],
    keywords="",
    packages=["hatchet_vis"],
    install_requires=[
        "ipykernel"
    ]
)