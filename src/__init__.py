from tweepydl import download
from scrape import scrape
import sys

tag = []
filename = "all_ids.json"

if len(sys.argv) >= 2:
    for i in range(len(sys.argv)):
        if (sys.argv[i][0] == '-'):
            tag.append(sys.argv[i])

if ("-h" in tag):
  
    print("birdysis: Scrapes and downloads liked tweets on Twitter.")
    print("Syntax: python __init__.py <argument>")
    print("Arguments: ")
    print(" -h: Prompt help menu.")
    print(" -f: Automatically retrives account information from userinfo.json. Created on normal execution.")
    print(" -d: Downloads tweets after scraping.")

    sys.exit()

elif ("-f" in tag):
    scrape("-f")

if ("-d" in tag):
    print('Proceeding to download tweets.')
    download(filename)


print("Goodbye!")


