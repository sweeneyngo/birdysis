from tweepydl import download
from scrape import scrape
import sys

tag = ""
if len(sys.argv) >= 2:
    tag = sys.argv[1]

scrape(tag)
print("Goodbye.")

