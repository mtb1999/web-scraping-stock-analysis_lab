import pandas as pd
import requests
from bs4 import BeautifulSoup
from data_extracting import parse_table

def html_scraping(url):
    netflix_data = requests.get(url).text
    netflix_soup = BeautifulSoup(netflix_data, 'html5lib')
    return netflix_soup