import requests
from bs4 import BeautifulSoup

url='https://ko.wikipedia.org/wiki/절기'
r=requests.get(url)
#print(r.text)
soup=BeautifulSoup(r.text, 'html.parser')
#print(soup) #currently, soup is the html text.

content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
#print(content_div) # in HTML, 'id

i = 1
for element in content_div.find_all("p", recursive=False):
    #print(element)
    print(element.getText())
    i += 1
