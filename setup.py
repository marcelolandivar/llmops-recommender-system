from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="llmops_recommendation_system",
    version="0.1",
    author="Marcelo",
    packages=find_packages(),
    install_requires=requirements,
)