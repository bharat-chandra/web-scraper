import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pandas as pd
l=[]
d=dict()
def scraper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    try:
        for i in range(150):
            # findAll('h3','class' : 'class name')
            # h3 is tag name
            # class name is class identifier for that tag.
            #i is the range i.e. it is the no.of lines to be scraped for that particular tag.
            one_a_tag = soup.findAll('h3',attrs = {'class':'name'})[i].text
            # .text extracts the text from that tag 
            one_a_tag=str(one_a_tag)
            l=one_a_tag.split()
            d[i]=''.join(l)
    except:
        pass
    df = pd.DataFrame(d.items(),columns=['col.1.','col.2.'])
    df.to_csv('scrape.csv', index=True, encoding='utf-8')
def(url='   ')

#pass the url to be scraped as the argument.
