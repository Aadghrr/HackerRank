import requests, datetime
from bs4 import BeautifulSoup

fptr = open('readme.md','w')

r = requests.get("https://www.hackerrank.com/darraghtobin"
    ,headers={'User-Agent':'Custom'})
soup = BeautifulSoup(r.text,'lxml')
badgeList = soup.find_all('div',{'class':'badges-list'})[0]
badgeTitles = badgeList.find_all('text',{'class':'badge-title'})
stars = badgeList.find_all('g',{'class':'star-section'})

fptr.write('HackerRank Skills as of '+datetime.datetime.now().isoformat()+'\n\n')
for i in range(len(stars)):
    k = badgeTitles[i].getText()
    v = len(stars[i].find_all('svg',{'class':'badge-star'}))
    fptr.write(k+' : '+str('*'*v)+'\n')
fptr.close()
