# Take the HN JSON file and dump it as separate files for mallet.

from bs4 import BeautifulSoup
import json
import sys

f = open('../ihearthn.json')
j = json.load(f)

oops = 0

for record in j['hits']:
    cid = record['objectID']
    html = record['comment_text']
    soup = BeautifulSoup(html)
    text = soup.getText()


    print cid
    print text.encode("utf-8")

    f_out = open('all/{}'.format(cid), 'w')
    f_out.write(text.encode("utf-8"))
    f_out.close()


