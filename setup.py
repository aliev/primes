from mypyc.build import mypycify
from setuptools import setup

setup(
    name="primes",
    packages=["primes"],
    ext_modules=mypycify(
        [
            "primes/__init__.py",
            "primes/utils.py",
        ]
    ),
    install_requires=[
        "wheel",
        "build",
        "mypy",
        "mypy-extensions",
    ],
)
