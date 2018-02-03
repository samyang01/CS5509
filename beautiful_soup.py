import requests
import bs4


res = requests.get('https://en.wikipedia.org/wiki/Cross_country_running')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
title = soup.select('div > h1')
new_File = open('title_body.txt', 'w')
for i in range(len(title)):
    new_File.write(title[i].getText() +'\n')
body = soup.select('div  [class=mw-content-ltr]')
for i in range(len(body)):
    new_File.write(body[i].getText() + '\n')

'''references:
https://www.w3.org/TR/CSS21/selector.html%23id-selectors'''