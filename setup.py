import setuptools
import os

this = os.path.abspath(os.path.dirname(__file__))
repo = "https://github.com/sweeneyngo/birdysis"

setuptools.setup(

    # Application name:
    name="birdysis",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Sweeney Ngo",
    author_email="sweeneyngo@gmail.com",

    # Packages
    packages=setuptools.find_packages(),

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        ],

    python_requires='>=3.6',

    # Include additional files into the package
    include_package_data=True,

    # Details
    url=repo,


    license="LICENSE",
    description="Retrieves and downloads liked tweets on Twitter.",

    # long_description=Readme,
    # long_description_content_type="text/markdown",

    # Dependent packages (distributions)
    install_requires=[
        "tweepy",
        "selenium",
        "cryptography",

    ],
    entry_points={
        'console_scripts': [
                'birdysis=src.__main__:main',
            ],
        },
)
