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

