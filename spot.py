# import 所需套件
from __future__ import with_statement
import contextlib
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

try:
    from urllib.request import urlopen
except:
    from urllib2 import urlopen

import sys

from random import random

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time


def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')


class Spot_keyword:
    def __init__(self, place):
        self.place = place

    def scrape(self):
        ua = UserAgent()
        user_agent = ua.safari
        headers = {'User-Agent': user_agent}

        response = requests.get(
            "https://www.tripadvisor.com.tw/Search?q=" + self.place +
            "&searchSessionId=1853EB8A25017B2676CC99E99AE5C0B71671986400450ssid&searchNearby=false&geo=293913&sid=3D04B97BBD1746929A37CB9D7EBF210C1671986408142&blockRedirect=true&rf=10&ssrc=A", headers=headers)

        soup = BeautifulSoup(response.content, "html.parser")

        cards = soup.find_all(
            'div', {'class': 'ui_columns is-mobile result-content-columns'}, limit=3)
        content = []
        result = []
        c = ""
        for card in cards:
            title = card.find("div", {"class": "result-title"}).getText()

            comment = card.find("div", {"class": "review-snippet-block"}).getText()

            add = card.find("div", {"class": "address"}).getText()

            try:
                url = card.find("a")
                url = 'https://www.tripadvisor.com.tw' + url["href"]
                url = make_tiny(url)

            except:
                url = 'https://www.tripadvisor.com.tw'

            c += f"{title} \n{add} \n{comment} \n\n"

        return c