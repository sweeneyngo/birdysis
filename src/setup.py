from distutils.core import setup

setup(
    # Application name:
    name="birdysis",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Sweeney Ngo",
    author_email="sweeneyngo@gmail.com",

    # Packages
    packages=["src"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/birdysis_v010/",

    #
    # license="LICENSE.txt",
    description="Retrieves and downloads liked tweets on Twitter.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "tweepy",
        "selenium",
        "cryptography",

    ],
)
