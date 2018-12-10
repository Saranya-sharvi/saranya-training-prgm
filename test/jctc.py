from bs4 import BeautifulSoup
import requests
import json

class Jctc:

	def title(soup):
		x=soup.find('title')
		return x.get_text()
		
	def doi(soup):
		y=soup.find("div",attrs={"id":"doi"})
		return y.get_text()
		
	def abstract(soup):
		z=soup.find("p",attrs={"class":"articleBody_abstractText"})		
		return z.get_text()

	def access(soup):
		at=access=soup.find("a",attrs={"class":"expander openaccess"})
		return at.get_text()
		
	def html(soup):
		hurl="https://pubs.acs.org/doi/full/10.1021/acs.jctc.8b00280"
		return hurl
		
		
	def current_issue(soup):
		curiss="https://pubs.acs.org/toc/jctcce/current"
		return curiss
		
	def date_ofissue(soup):											
		s=soup.find("div",attrs={"id":"764a4ee4-9265-43f8-8a38-36480fcd64fa"})	
		#for date in s:
		#	if (s.get_text()) != '\n':
		return s.get_text()		
			
	def pub_type(soup):
		p=soup.find("div",attrs={"class":"manuscriptType"})	
		
	#	for info in p:
	#		if (p.get_text()) != "\n":

		return p.get_text()
		
		
	

	
inp=requests.get("https://pubs.acs.org/doi/pdf/10.1021/acs.jctc.8b00280")		
		
 
def Jctc_out(inp):

	soup=BeautifulSoup(inp.content, "lxml")
	crawel={}
	crawel['pub_type'] = Jctc.pub_type(soup)
	crawel['title'] = Jctc.title(soup)
	crawel['doi'] = Jctc.doi(soup)
	crawel['abstract'] = Jctc.abstract(soup)
	crawel['accesstype'] = Jctc.access(soup)
	crawel['html_url'] = Jctc.html(soup)
	crawel['current_issue'] = Jctc.current_issue(soup)
	#crawel['authors'] = Jctc.author(soup)
	#crawel['institute'] = Jctc.inst(soup)
	#crawel['auth_inst'] = Jctc.author_inst(soup)
	crawel['issue_date'] = Jctc.date_ofissue(soup)
	return crawel

out_json = Jctc_out(inp)
print(out_json)
with open('jctcsite.json', 'w')as jctc:
	json.dump(out_json, jctc) 




"""	def author(soup):
		authors=[]
		a=soup.find("div",attrs={"id":"authors"})
		authors_array=(a.find_all("a"))
		
		for information in authors_array:
		
			if (information.get_text()) != '*':
				auth = {}
				
				auth['name']=information.get_text()
				#auth['id'] = 
				authors.append(auth)
				
		
		return authors			

	def inst(soup):
		institute = []
		u=soup.find("div",attrs={"id":"aff1"})
		inst = {}
		
		inst['name']=u.get_text()
		#inst['id'] = 
		
		institute.append(inst)
		
		return institute

 
 
	def author_inst(soup):
		auth_ins_list=[]
		author=Jctc.author(soup)
		institute =Jctc.inst(soup)
		
		if author == auth
		
		ans = author+institute
		auth_ins_list.append(ans)
		return auth_ins_list
	
	
	
aut=soup.find_all("div id""articleMeta",attrs={"span class":"hlFld-ContribAuthor"})
aut=soup.find("div",attrs={"id":"articleMeta"})
print(aut)"""
		

		
		
"""<div id="articleMeta">
<	div id="authors">
	<span class="hlFld-ContribAuthor">
		<span class="hlFld-ContribAuthor">
			<a id="authors" href="/author/Ekimoto%2C+Toru">Toru Ekimoto</a>
		</span>
		<span>
		<span class="NLM_xref-aff">
			<sup>†</sup>
		</span>
		</span>
	</span>
	<span>
		<span class="NLM_x">
			<x xmlns:oasis="http://www.niso.org/standards/z39-96/ns/oasis-exchange/table" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ali="http://www.niso.org/schemas/ali/1.0/" xml:space="preserve">, </x>
		</span>
	</span>
	
	
	<span class="hlFld-ContribAuthor">
		<span class="hlFld-ContribAuthor">
			<a id="authors" href="/author/Yamane%2C+Tsutomu">Tsutomu Yamane</a>
		</span>
	<span>
	<span class="NLM_xref-aff">
		<sup>†</sup>
	</span>
	</span>
	</span>
	<span>
		<span class="NLM_x">
			<x xmlns:oasis="http://www.niso.org/standards/z39-96/ns/oasis-exchange/table" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ali="http://www.niso.org/schemas/ali/1.0/" xml:space="preserve">, and </x>
		</span>
	</span>


	<span class="hlFld-ContribAuthor">
		<span class="hlFld-ContribAuthor">
			<a id="authors" href="/author/Ikeguchi%2C+Mitsunori">Mitsunori Ikeguchi</a>
		</span>
	<span>
		<a class="ref" href="#cor1">*</a>
	</span>
	<span>
		<span class="NLM_xref-aff">
		<sup>†</sup>
	</span>
	</span>
	<span>
		<span class="NLM_xref-aff">
		<sup>‡</sup>
	</span>
	</span>
	<span class="orcid-link-icon">
 		<a href="http://orcid.org/0000-0003-3199-6931" target="_blank">
 		<img src="/templates/jsp/images/orcid.png" />
 		</a>
 	</span>
 	</span>
 </div>
 
 
 
 <div class="affiliations">
 <div id="aff1">

 <sup>†</sup> 

 <span class="institution">Graduate School of Medical Life Science</span>, 
 <institution-wrap xmlns:oasis="http://www.niso.org/standards/z39-96/ns/oasis-exchange/table" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ali="http://www.niso.org/schemas/ali/1.0/">
 <span class="institution">Yokohama City University</span>
 </institution-wrap>, 
 <span class="addr-line">1-7-29 Suehiro-cho, Tsurumi-ku</span>, 
 <city xmlns:oasis="http://www.niso.org/standards/z39-96/ns/oasis-exchange/table" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ali="http://www.niso.org/schemas/ali/1.0/">Yokohama</city> 
 <postal-code xmlns:oasis="http://www.niso.org/standards/z39-96/ns/oasis-exchange/table" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ali="http://www.niso.org/schemas/ali/1.0/">230-0045</postal-code>,
<span class="country">Japan</span>
</div>

<div id="aff2">

<sup>‡</sup>


 <span class="institution">RIKEN Medical Sciences Innovation Hub Program</span>, 
<span class="addr-line">1-7-22 Suehiro-cho, Tsurumi-ku</span>, 
<city xmlns:oasis="http://www.niso.org/standards/z39-96/ns/oasis-exchange/table" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ali="http://www.niso.org/schemas/ali/1.0/">Yokohama</city>
 <postal-code xmlns:oasis="http://www.niso.org/standards/z39-96/ns/oasis-exchange/table" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ali="http://www.niso.org/schemas/ali/1.0/">230-0045</postal-code>, 
 <span class="country">Japan</span>
 </div>
 </div>
 
""" 
 
 

