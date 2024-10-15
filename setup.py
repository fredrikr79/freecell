from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="freecell",
    version="1.0",
    description="Freecell Solitaire in Pygame with Nix",
    license="GNU GENERAL PUBLIC LICENSE",
    long_description=long_description,
    author="fredrikr79",
    author_email="fredrikrobertsen7@gmail.com",
    packages=["src/core", "src/ui"],
    # install_requires=[],  # handled by nix-shell
    scripts=[],
)
