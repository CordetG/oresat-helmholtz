import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="helmholtz-cage",
    version="1.0.0",
    author="Dmitri McGuckin",
    author_email="dmitri.mcguckin26@gmail.com",
    description="A GUI-Based controller for the OreSat helmlotz magnetic cage.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oresat/oresat-helmholtz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
