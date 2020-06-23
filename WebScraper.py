import urllib.request
from bs4 import BeautifulSoup
import requests
import pprint

URL = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(class_ = "VDXfz")

news_elems = soup.find_all('h3', class_='ipQwMb ekueJc gEATFF RD0gLb')

for news_elem in news_elems:
    #print(news_elem, end='\n'*2)
    title_elem = news_elem.find('a', class_='DY5T1d')
    print(title_elem.text)
