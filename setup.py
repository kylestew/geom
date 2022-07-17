from setuptools import setup

setup(
    name="geom",
    version="0.0.1",
    author="Kyle Stewart",
    author_email="kylestew@gmail.com",
    packages=["geom"],
    description="A geometry data and functions library",
    long_description=open("README.md").read(),
    install_requires=["scipy", "numpy", "shapely", "iteration_utilities"],
)
