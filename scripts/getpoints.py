__author__ = 'tbarik'

from bs4 import BeautifulSoup
import json
import sys

f = open('../ihearthn.json')
j = json.load(f)

for record in j['hits']:
    print record['points']