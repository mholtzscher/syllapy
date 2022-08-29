from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="syllapy",
    version="0.7.2",
    url="https://github.com/mholtzscher/syllapy",
    license="MIT",
    author="Michael Holtzscher",
    author_email="michael.holtzscher@gmail.com",
    description="Calculate syllable counts for English words.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["syllables", "nlp"],
    python_requires=">=3.6, <4",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
)
