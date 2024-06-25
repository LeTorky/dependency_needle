from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="dependency_needle",
    version="1.1.1",
    description="Dependency injection container",
    author="Your Name",
    author_email="24torky@gmail.com",
    packages=find_packages(),
    install_requires=requirements
)
