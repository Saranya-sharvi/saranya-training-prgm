import re
from bs4 import BeautifulSoup

with open("index.html") as fp:

		
	soup = BeautifulSoup(fp, "lxml")
	#print(soup)
	#for s in soup.find_all("a", attrs={"class": "sister"}):
	#	print(s) 
		#for p in soup.find_all("a"):
		#	print(p['href'])"""
	#g=(soup.find_all("a", abc={"class": "sister"}))
	#print(g)
	#print(soup.find_all("a", limit=0))
	
	
	#print(soup.html.find_all("title"))

	
	#print(soup.html.find_all("title", recursive=False))	
	
	#for v in string.find_parents("p"):
	#print(soup.select("#link1 ~ .sister"))


	"""def uppercase(str):
		return str.upper()
	print(soup.prettify(formatter=uppercase))"""
	
	y=soup.get_text()
	print(y)





		
	#soup.find_all(string="Elsie")
	#soup =("soup.title", "lxml")
	#type(tag)

	#page_link=len(soup.contents)
	#head = soup.head
	#print(soup)
	"""title_tag = soup.title
	title_tag = title_tag.string
	print(title_tag)"""
	#for string in soup.stripped_strings:
	#	print(repr(string))
	
	#print(soup.html.string)
	#title_tag = soup.title
	#title_tag.string.parent
	#print(title_tag)
	#for child in title_tag.children:
	#	print(child)
	
	#for child in head_tag.descendants:
	#	print(child)
    
	#for child in title_tag.children:
	#	print(child)
	
	
	"""html_tag = soup.html
	type(html_tag.parent)
	print(type(html_tag.parent))
"""	
	
	
	#print("title is:", title_tag.get_text())
	#print(page_link)
	"""children = id.findChildren("p", recursive=False)
	for child in children:
		print(child)"""


"""link = soup.a
#link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
# p
# body
# html
# [document]
# None"""
"""sibling_soup = soup.sibling
sibling_soup.b.next_sibling
print(sibling_soup)"""


#sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></a>", "lxml")
#print(sibling_soup.prettify())
#h=sibling_soup.b.next_sibling 
#A=sibling_soup.c.previous_sibling
#print(A)

"""link = soup.a
link
l=link.next_sibling.next_sibling
print(l)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

link.next_sibling
# u',\n'"""

#for sibling in soup.a.next_siblings:
 #   print(repr(sibling))
 
#for sibling in soup.find(id="link3").previous_siblings:
#	print(repr(sibling))

last_a_tag = soup.find("a", id="link3")
#last_a_tag
#print(last_a_tag)

#w=last_a_tag.next_sibling
#print(w)
#s=last_a_tag.previous_element
#s=last_a_tag.previous_element.next_element
#s=last_a_tag.next_element
#print(s)
# u'Tillie'

#for element in last_a_tag.next_elements:
 #   print(repr(element))


#f=soup.find_all('b')
#print(f)
#import re
"""for tag in soup.find_all(re.compile("^b")):
    print(tag.name)"""


"""for tag in soup.find_all(re.compile("t")):
    print(tag.name)"""
"""a=soup.find_all(["a", "b"])
print(a)"""

"""for tag in soup.find_all(True):
    print(tag.name)"""

"""def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
v=soup.find_all(has_class_but_no_id)
print(v)"""

"""
def not_lacie(href):
    return href and not re.compile("lacie").search(href)
s=soup.find_all(href=not_lacie)
print(s)"""



"""from bs4 import NavigableString
def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))

for tag in soup.find_all(surrounded_by_strings):
    print(tag.name)"""
    
#print(soup.find(string=re.compile("sisters")))
#t=soup.find_all(id = "link3")
#print(y)
#print(soup.find_all(href=re.compile("elsie")))
#print(soup.find_all(id=True))
#print(soup.find_all(href=re.compile("elsie"), id='link1'))
"""r=soup.find_all(attrs={"data-foo": "value"})"""
#print(soup.find_all("a", class_="sister"))





"""def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6
print(soup.find_all(class_=has_six_characters))

#print(soup.find_all(class_=re.compile("itl")))
"""
#css_soup = BeautifulSoup("")
#print(css_soup)







