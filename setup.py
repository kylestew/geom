from setuptools import setup, find_packages

setup(
    name="geom",
    version="0.0.48",
    author="Kyle Stewart",
    author_email="kylestew@gmail.com",
    packages=find_packages(),
    description="A geometry data and functions library",
    long_description=open("README.md").read(),
    install_requires=[
        "scipy",
        "numpy",
        "shapely",
        "iteration_utilities",
        "bezier",
    ],
)
