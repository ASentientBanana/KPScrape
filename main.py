import requests 
from bs4 import BeautifulSoup
import time
import lxml
import json
import re

JData = {
    'Items':[

    ]
}

# -*- coding: utf-8 -*-
inp = "wacom"
URL = "https://www.kupujemprodajem.com/search.php?action=list&data%5Bpage%5D=1&data%5Bprev_keywords%5D="+inp+"&data%5Border%5D=relevance&submit%5Bsearch%5D=Tra%C5%BEi&dummy=name&data%5Bkeywords%5D="+inp

Req = requests.get(URL)
ReqF = Req.text
Hfile =open("index.html", 'w')

soup = BeautifulSoup(ReqF, "html5lib")
soup.prettify()
fin = soup.find("div",{'id':"adListContainer"} )
Name = fin.find_all("a",{'class':'adName'})
Image = fin.find_all("div",{'class':'adImgWrapper'})
Price = fin.find_all("span",{'class':'adPrice'})
NameAndImg = []
Prices = []
jsonfile = open('data.json', mode='w')

TTR = open('temp.txt','w')
print('')
newline = '\n'
for kk in Price:
 
    kkk = kk.text.strip()
  
    Prices.append(kkk)

counter = 0
for i in Image:

    for I in Prices:

        ii = I.replace(u'\xa0', ' ')
        NameAndImg.append( [i.img['alt'], i.img['src'],ii])

        for u in NameAndImg:
            
            json.dump(u,jsonfile)
            break
       
        break
    counter += 1
