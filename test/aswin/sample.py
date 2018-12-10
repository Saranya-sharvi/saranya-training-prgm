from bs4 import BeautifulSoup
import requests
input = requests.get("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
reddit1Content =BeautifulSoup(input.content,"lxml")

a=reddit1Content.find('title')
print(a.get_text())
