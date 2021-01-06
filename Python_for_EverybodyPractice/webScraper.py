from urllib import request,parse,error
from bs4 import BeautifulSoup


url = input("Enter the url: ")
html=request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

tags=soup('a')
for tag in tags: 
    print(tag.get('href',None))
