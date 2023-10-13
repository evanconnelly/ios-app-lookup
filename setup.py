from setuptools import setup

setup(
    name="ios-lookup",
    version="0.1",
    py_modules=["ios_lookup"],
    install_requires=[
        "requests",
    ],
    entry_points={
        'console_scripts': [
            'ios-lookup = ios_lookup:main',
        ],
    },
)
