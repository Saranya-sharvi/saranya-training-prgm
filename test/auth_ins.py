from bs4 import BeautifulSoup
import requests
import json

class crawel:
	
	def auth(soup):
		authors_list=[]
		
		a=soup.find("div", attrs={"id":"authors"})

		for auth_list in a.find_all("span", attrs={"class":"hlFld-ContribAuthor"}):
			auth_id = {}
			if (auth_list.find("span", attrs={"class":"NLM_xref-aff"})):
				ins_id = []
				for aut in auth_list:
					if (aut.find("a",attrs={"id":"authors"})):				
						author = aut.find("a",attrs={"id":"authors"})
						auth_id["name"] = author.get_text()
					
					institute = aut.find_all("span", attrs={"class":"NLM_xref-aff"})
					
					for inst in institute:
						
						if (inst.find("sup")):
							ins_id.append(inst.get_text())
							
				auth_id["aff_id"] = ins_id

			if auth_id!={}:
				authors_list.append(auth_id)
											
		return authors_list
		
				
	def institution(soup):
		institution_list=[]
		i1=soup.find("div",attrs={"class":"affiliations"})
		y = i1.find_all("div")
		for i in y:
			institute = {}
			institute["aff_id"] = i.find("sup").get_text()
			institute["city"] = i.find("city").get_text()
			institute["country"] = i.find("span",attrs={"class":"country"}).get_text()
			institute["ins_name"] = " "
			
			ins = i.find_all("span",attrs={"class":"institution"})
			
			if len(ins)>1:
				name_list = []
				for inst in ins:
					name = inst.get_text()
					new = name.replace("\r\n", " ")
					name_list.append(new)
				institute["ins_name"] = ','.join(name_list)
				
		
			else:
				name = ins[0].get_text()
				new = name.replace("\r\n", " ")
				
				institute["ins_name"] = new			
			
			institution_list.append(institute)

		return institution_list

	def auth_inst(soup):
		authors = crawel.auth(soup)
		#print(authors)
		institutes = crawel.institution(soup)
		#print(institutes)
		#affid = institutes["aff_id"]
		auth_inst_list=[]
		
		for i, auth in enumerate(authors):
			author_dict = {}
			author_dict["name"] = auth["name"]
			inst_list = []
			if len(auth["aff_id"])>1:
				
				for j, inst in enumerate(institutes):
					new_ins = {}
					for ids in auth["aff_id"]:
						if ids == inst["aff_id"]:
							new_ins["Ins_name"] = inst["ins_name"]
							new_ins["city"] = inst["city"]
							new_ins["country"] = inst["country"]
							
					inst_list.append(new_ins)
					
				author_dict["institute"] = inst_list
				
			else:
				
				for j, inst in enumerate(institutes):
					new_ins = {}
					if auth["aff_id"][0] == inst["aff_id"]:
						new_ins["Ins_name"] = inst["ins_name"]
						new_ins["city"] = inst["city"]
						new_ins["country"] = inst["country"]
						
						#inst_list.inst[institute_name]
					if new_ins != {}:	
						inst_list.append(new_ins)
				
				author_dict["institute"] = inst_list
					
					
			auth_inst_list.append(author_dict)
					
					
		#print(auth_inst_list)			
		return auth_inst_list	
		
		
inp=requests.get("https://pubs.acs.org/doi/pdf/10.1021/acs.jctc.8b00280")	
#print(inp.content)	
def out(inp):
	soup=BeautifulSoup(inp.content, "lxml")
	#print(soup)
	ans = {}
	ans['auth'] = crawel.auth(soup)
	ans['institution'] = crawel.institution(soup)
	#print(ans)
	out_json = crawel.auth_inst(soup)
	print(out_json)

	with open('parse.json', 'w')as jctc:
		json.dump(out_json, jctc)	
	
	
out(inp)

"""[<div class="affiliations">

<div id="aff1">
<sup>†</sup> 
<span class="institution">Graduate
School of Medical Life Science
</span>, 
<institution-wrap xmlns:ali="http://www.niso.org/schemas/ali/1.0/" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:oasis="http://www.niso.org/standards/z39-96/ns/oasis-exchange/table" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<span class="institution">Yokohama
City University
</span>
</institution-wrap>,
<span class="addr-line">1-7-29 Suehiro-cho, Tsurumi-ku</span>, 
<city xmlns:ali="http://www.niso.org/schemas/ali/1.0/" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:oasis="http://www.niso.org/standards/z39-96/ns/oasis-exchange/table" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">Yokohama
</city>
<postal-code xmlns:ali="http://www.niso.org/schemas/ali/1.0/" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:oasis="http://www.niso.org/standards/z39-96/ns/oasis-exchange/table" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">230-0045
</postal-code>, 
<span class="country">
Japan
</span>
</div>

<div id="aff2">
<sup>‡</sup> 
<span class="institution">
RIKEN
Medical Sciences Innovation Hub Program
</span>, 
<span class="addr-line">1-7-22 Suehiro-cho, Tsurumi-ku</span>,
<city xmlns:ali="http://www.niso.org/schemas/ali/1.0/" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:oasis="http://www.niso.org/standards/z39-96/ns/oasis-exchange/table" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
Yokohama</city>
<postal-code xmlns:ali="http://www.niso.org/schemas/ali/1.0/" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:oasis="http://www.niso.org/standards/z39-96/ns/oasis-exchange/table" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">230-0045
</postal-code>, 
<span class="country">Japan
</span>
</div>
</div>]"""
			
			
"""
<div id="authors">
<span class="hlFld-ContribAuthor">
<span class="hlFld-ContribAuthor">
<a href="/author/Ekimoto%2C+Toru" id="authors">Toru Ekimoto</a>
</span>
<span>
<span class="NLM_xref-aff">
<sup>†</sup>
</span>
</span>
</span>
<span>
<span class="NLM_x"><x xml:space="preserve" xmlns:ali="http://www.niso.org/schemas/ali/1.0/" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:oasis="http://www.niso.org/standards/z39-96/ns/oasis-exchange/table" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">, </x>
</span>
</span>

<span class="hlFld-ContribAuthor">
<span class="hlFld-ContribAuthor">
<a href="/author/Yamane%2C+Tsutomu" id="authors">Tsutomu Yamane</a>
</span><span>
<span class="NLM_xref-aff">
<sup>†</sup>
</span>
</span></span>
<span>
<span class="NLM_x">
<x xml:space="preserve" xmlns:ali="http://www.niso.org/schemas/ali/1.0/" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:oasis="http://www.niso.org/standards/z39-96/ns/oasis-exchange/table" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">, and </x></span></span>

<span class="hlFld-ContribAuthor">
<span class="hlFld-ContribAuthor">
<a href="/author/Ikeguchi%2C+Mitsunori" id="authors">Mitsunori Ikeguchi</a>
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

<span class="orcid-link-icon"> <a href="http://orcid.org/0000-0003-3199-6931" target="_blank"><img src="/templates/jsp/images/orcid.png"/></a></span></span></div>

"""




"""
[<span class="hlFld-ContribAuthor">
<span class="hlFld-ContribAuthor">
<a href="/author/Ekimoto%2C+Toru" id="authors">Toru Ekimoto</a></span><span><span class="NLM_xref-aff"><sup>†</sup></span></span></span>, <span class="hlFld-ContribAuthor"><a href="/author/Ekimoto%2C+Toru" id="authors">Toru Ekimoto</a></span>, <span class="hlFld-ContribAuthor"><span class="hlFld-ContribAuthor"><a href="/author/Yamane%2C+Tsutomu" id="authors">Tsutomu Yamane</a></span><span><span class="NLM_xref-aff"><sup>†</sup></span></span></span>, <span class="hlFld-ContribAuthor"><a href="/author/Yamane%2C+Tsutomu" id="authors">Tsutomu Yamane</a></span>, <span class="hlFld-ContribAuthor"><span class="hlFld-ContribAuthor"><a href="/author/Ikeguchi%2C+Mitsunori" id="authors">Mitsunori Ikeguchi</a></span><span><a class="ref" href="#cor1">*</a></span><span><span class="NLM_xref-aff"><sup>†</sup></span></span><span><span class="NLM_xref-aff"><sup>‡</sup></span></span><span class="orcid-link-icon"> <a href="http://orcid.org/0000-0003-3199-6931" target="_blank"><img src="/templates/jsp/images/orcid.png"/></a></span></span>, <span class="hlFld-ContribAuthor"><a href="/author/Ikeguchi%2C+Mitsunori" id="authors">Mitsunori Ikeguchi</a></span>]


"""


"""
<div id="authors"><span class="hlFld-ContribAuthor"><span class="hlFld-ContribAuthor">
<a id="authors" href="/author/Harada%2C+Ryuhei">Ryuhei Harada</a></span><span>
<a casls="ref" href="#cor1">*</a></span>
<span class="orcid-link-icon"> <a href="http://orcid.org/0000-0001-7987-0540" target="_blank">
<img src="/templates/jsp/images/orcid.png" />
</a></span></span><span><span class="NLM_x"><x xmlns:oasis="http://www.niso.org/standards/z39-96/ns/oasis-exchange/table" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ali="http://www.niso.org/schemas/ali/1.0/" xml:space="preserve"> 
and </x>
</span></span>
<span class="hlFld-ContribAuthor">
<span class="hlFld-ContribAuthor"><a id="authors" href="/author/Shigeta%2C+Yasuteru">Yasuteru Shigeta</a></span><span><a class="ref" href="#cor2">*</a></span><span class="orcid-link-icon"> <a href="http://orcid.org/0000-0002-3219-6007" target="_blank"><img src="/templates/jsp/images/orcid.png" /></a></span></span></div>

<div class="affiliations"><div id="aff1"><span class="institution">Center for Computational
Sciences</span>, <institution-wrap xmlns:oasis="http://www.niso.org/standards/z39-96/ns/oasis-exchange/table" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ali="http://www.niso.org/schemas/ali/1.0/"><span class="institution">University of Tsukuba</span></institution-wrap>, <span class="addr-line">1-1-1 Tennodai</span>, <city xmlns:oasis="http://www.niso.org/standards/z39-96/ns/oasis-exchange/table" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ali="http://www.niso.org/schemas/ali/1.0/">Tsukuba</city>, <state xmlns:oasis="http://www.niso.org/standards/z39-96/ns/oasis-exchange/table" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ali="http://www.niso.org/schemas/ali/1.0/">Ibaraki</state> <postal-code xmlns:oasis="http://www.niso.org/standards/z39-96/ns/oasis-exchange/table" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ali="http://www.niso.org/schemas/ali/1.0/">305-8577</postal-code>, <span class="country">Japan</span></div></div><div class="wrapper"><div class="generic-sec"><div id="citation">div>
 """ 
    
        
    
        
    
        
    
        
    
        
    
        
            
            
            
        
    
        
    
        
    
        
    
        
    
        
    
    
    

    
