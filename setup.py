import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work'
setup(
    name="ptrmetagen",
    version='1.0.0',
    description="Package inludes tools for Tondor",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/gisat/tondor_tools",
    author="Michal Opetal, Sivasankar Arul",
    author_email="michal.opletal@gisat.cz, sivasankar.arul@gisat.cz",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9"],
    packages=["tondor-tool"],
    package_data = {'tiles_gpkg': ['*.gpkg']},
    include_package_data=True
    )