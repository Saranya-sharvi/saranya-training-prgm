from bs4 import BeautifulSoup
import requests
import json

class Jctc:

	def title(soup):
		x=soup.find('title')
		x1=x.get_text()
		#print(x1)
		return x1
		
	def doi(soup):
		y=soup.find("div",attrs={"id":"doi"})
		y1=y.get_text()
		#print(y1)
		return y1
		
	def abstract(soup):
		z=soup.find("p",attrs={"class":"articleBody_abstractText"})	
		z1=z.get_text()	
		#print(z1)
		return z1

	def access(soup):
		at=access=soup.find("a",attrs={"class":"expander openaccess"})
		at1=at.get_text()
		#print(at1)
		return at1
		
	def html(soup):
		hurl="https://pubs.acs.org/doi/full/10.1021/acs.jctc.8b00280"
		#print(hurl)
		return hurl
		
		
	def current_issue(soup):
		curiss="https://pubs.acs.org/toc/jctcce/current"
		print(curiss)
		return curiss
		
	def date_ofissue(soup):											
		s=soup.find("div",attrs={"id":"764a4ee4-9265-43f8-8a38-36480fcd64fa"})	
		s1=s.get_text()	
		#print(s1)
		#for date in s:
		#	if (s.get_text()) != '\n':
		return s1
			
	def pub_type(soup):
		p=soup.find("div",attrs={"class":"manuscriptType"})	
		p1=p.get_text()
		
	#	for info in p:
	#		if (p.get_text()) != "\n":
		#print(p1)
		return p1
		
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
		authors = Jctc.auth(soup)
		#print(authors)
		institutes = Jctc.institution(soup)
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
	crawel['auth'] = Jctc.auth(soup)
	crawel['institute'] = Jctc.institution(soup)
	crawel['auth_inst'] = Jctc.auth_inst(soup)
	crawel['issue_date'] = Jctc.date_ofissue(soup)
	
	
	print(crawel)
	with open('jctcsite.json', 'w')as jctc:
		json.dump(crawel, jctc) 

Jctc_out(inp)	
	
		

		

