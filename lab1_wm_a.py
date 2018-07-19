#print all src(absolute and relative) of images in the given website only using requests

import re
import requests
import csv

f=csv.writer(open('image_links.csv','w'))
f.writerow(['link','sno'])
r = requests.get("http://books.toscrape.com/")
r = r.text

sno=0
for i in r.split('"'):
        if re.search('png',i) or re.search('gif',i) or re.search('jpg',i):
                if 'http' in i or 'https' in i:
                        f.writerow([i],sno)
                        print(i)
                else:
                        f.writerow(['http://books.toscrape.com/'+i,sno])
                        print('http://books.toscrape.com/'+i)
