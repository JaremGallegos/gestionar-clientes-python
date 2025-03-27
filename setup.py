from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()
    
setup(
    name = "gestionar-clientes",
    version = "0.1.0",
    description = "Un proyecto para poder gestionar clientes de una empresa eCommerce",
    package_dir = {"": "src"},
    packages = find_packages(where = "src"),
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/JaremGallegos/gestionar-clientes-python.git",
    author = "JaremGallegos",
    author_email = "73142526@continental.edu.pe",
    license = "MIT"
)