#extracting all links on a web page
#can be altered to extract different items

import requests
import csv
from bs4 import BeautifulSoup


f=csv.writer(open('links.csv','w'))
f.writerow(['name','link'])
url = 'http://books.toscrape.com/'
try:
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'html.parser')
    a_links=soup.find_all('a')
    for l in a_links:
        try:
            name=l.contents[0]
        except:
            name=""
        add_link=l.get('href')
        if add_link=="index.html":
            link=url+add_link
        else:
            if 'http' in add_link or 'https:' in add_link:
                link=add_link
            else:
                link=url+add_link
        try:
            f.writerow([name,link])
        except:
            print("cannot write in file")
except:
    print("request to page failed")
