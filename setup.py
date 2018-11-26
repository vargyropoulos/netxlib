import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="netxlib",
    version="0.0.1",
    author="Vasilis Argyropoulos",
    author_email="ba_lykos@yahoo.com",
    description="A collection of network utilities for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vargyropoulos/netxlib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
