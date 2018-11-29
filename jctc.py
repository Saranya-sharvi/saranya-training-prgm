from bs4 import BeautifulSoup
import requests


inp=requests.get("https://pubs.acs.org/doi/pdf/10.1021/acs.jctc.8b00280")
soup=BeautifulSoup(inp.content, "lxml")
#print(source)
x=soup.find('title')
y=soup.find("div",attrs={"id":"doi"})
z=soup.find("p",attrs={"class":"articleBody_abstractText"})

a=soup.find("div",attrs={"id":"authors"})
authors_array=(a.find_all("a"))
for information in authors_array:
	#print(information.get_text())
	if information.get_text() != '*'and " ":
		print("Author name: ",information.get_text())
univ=soup.find("div",attrs={"id":"aff1"})
s=soup.find("div",attrs={"id":"764a4ee4-9265-43f8-8a38-36480fcd64fa"})

html_url="https://pubs.acs.org/doi/full/10.1021/acs.jctc.8b00280"
current_issue="https://pubs.acs.org/toc/jctcce/current"
access=soup.find("a",attrs={"class":"expander openaccess"})
journal=soup.find("a",attrs={"class":"expander"}) ['href']

 
print("Title: ",x.get_text())

print("Abstract:",z.get_text())

print(y.get_text())
	
print("Name and city of university: ",univ.get_text())

print("Accesstype: ",access.get_text())

print("html_url: ",html_url)
print("journal link: ","https://pubs.acs.org{}".format(inp))	
print("current_issue_url: ",current_issue)
print("Date_Received and Date_Published: ", s.get_text())












