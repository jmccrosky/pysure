import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pysure",
    version="0.1.0",
    description="Surrogate residuals for logistic regression",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jmccrosky/pysure",
    author="Jesse McCrosky",
    author_email="mccrosky@gmail.com",
    license="MIT",
    packages=["pysure"],
    package_dir={'': 'src'},
    include_package_data=True,
)
