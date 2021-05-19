## birdysis

 [![Python versions](https://img.shields.io/pypi/pyversions/birdysis.svg)](https://pypi.python.org/pypi/birdysis/) [![PyPI](https://img.shields.io/pypi/v/birdysis.svg)](https://pypi.python.org/pypi/birdysis/) [![Code style: flake8](https://img.shields.io/badge/code%20style-flake8-black)](https://github.com/PyCQA/flake8)
 
birdysis is a small library that compiles and downloads a specified amount of Twitter liked post(s).

## Purpose

Twitter lacked the functionality of readily seeing through your liked post(s), which was my modus operandi for saving pictures/videos from artists/creators I've greatly enjoyed. And frustratingly, [Twitter's Developer API](https://developer.twitter.com/en/products/twitter-api) can only grab/download a set amount of posts (max caps at [3200](https://stackoverflow.com/questions/64015641/how-to-get-3200-tweets-from-a-new-twitters-api-and-what-is-getoldtweets3-altern)).
With the additional bottleneck of its rate limiting, and the bizarre behavior of missing/dead posts throughout my Liked feed, I decided it was time to finally optimize archiving Twitter posts to a more accessible storage.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install birdysis.

```bash
pip install birdysis
```

- Currently, it uses a WebDriver to collect data from your Twitter feed, which is defaulted to Firefox. Additional driver(s) are required (specifically, [gekckodriver](https://github.com/mozilla/geckodriver/releases)).
- Install the appropriate package for your OS (preferably `.tar.gz`) and then do

```bash
tar -xvf <name_of_package.tar.gz>
mv geckodriver /usr/bin/

# just in case:
export PATH=$PATH:/usr/bin

```

## Preparation
birdysis uses [tweepy](https://docs.tweepy.org/en/latest/) to readily download files from Twitter's API by feeding in your liked IDs. In order to access the API,
some credentials are required. 

1. Head over to [Twitter's Developer Portal](https://developer.twitter.com/en), and sign in to your account.
2. Click Developer Portal on the right navigation bar.
3 Create a new Application, and go through the process until you're able to check out 'Keys and Tokens'.
4. Copy the Consumer Keys and Access Keys/Secret values, such that you can place them in `api_keys.json` as such:*

*Variable values are represented with <>.

```json
{
  "consumer_key": "<API_KEY>",
  "consumer_secret": "<API_SECRET>",
  "access_token": "<ACCESS_TOKEN>",
  "access_secret": "<ACCESS_SECRET>",
}
```

4. If necessary, place your JSON file in the same directory in which you wish to store/download your Liked IDs. 

## Usage

```python
from birdysis.collect_data import scrape
from birdysis.download import download

# for scrape
scrape()
# auto-login flag
scrape('-f')

# generated file must match exactly
download('all_ids.json')

```

## Goals

- Add more flags for default size, timeout, webDriver type, and media directory.
- Implement browser support for Google Chrome, Safari, and Opera.
- Conduct tests in different machines (verified in Ubuntu 20.04, Arch Linux 5.11.16).


## Contributing
Pull requests are always welcome! Any major changes you wish to implement should first be initiated with an issue + pull request (updating tests as necessary).

## Major Technologies
- [selenium](https://selenium-python.readthedocs.io/) (3.141.0)
- [tweepy](https://docs.tweepy.org/en/latest/) (3.10.0)
- shutil + requests (2.25.1)

## License
[MIT](https://choosealicense.com/licenses/mit/)
