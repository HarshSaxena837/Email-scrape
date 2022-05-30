import re
# from selenium import webdriver

import requests
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
import pandas as pd



url = "https://www.yelp.com/biz/roven-law-group-new-york-city"

Email_REGEX = r"[\w\.-]+@[\w\.-]+"

r = requests.get(url)

for re_match in re.findall(Email_REGEX, r.text):

    print(re_match)
