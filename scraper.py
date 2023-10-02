import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase
import pandas as pd
import re

url = "http://ufcstats.com/statistics/fighters?char="
end_url = "&page=all"
fighters = []
data = requests.get(url).text
# Create beautiful Soup object
soup = BeautifulSoup(data, 'html.parser')


def get_urls(target_url='http://ufcstats.com/statistics/fighters?char='):
    urls = []
    for char in ascii_lowercase:
        final_url = url + char + end_url
        urls.append(final_url)
    return urls


class FighterScraper:

    def fetch(self, url):
        print('HTTP GET request to URL: {}'.format(url))

        res = requests.get(url)