#!/usr/bin/env python3

#system level imports first
import sys
import re
import os
#global package imports next
import gzip
import json
import requests

# specific dependency modules next
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.request
from geotext import GeoText

#in-house custom module imports last
from almamater import out
from commonfunction import mainfun
from commonfunction import Commonfun as cf

#sciepub/json directory create method
paths=os.path.exists("sciepub/json/")
print(paths)
if paths==False:
    os.mkdir("sciepub/json/")


# USAGE :
# 	python3 sciepub_parser.py

#SAMPLE OUTPUT



class Article:

    def article_type(soup):
        '''
        Parse article_type for the given article URL Element
        '''
        for tag in soup.find_all('body'):
            tags=tag.find('span',attrs={'class':'bgj colorj fonthn fontsize12 ml5 pad0310'})
            if tags != None:
                article_type = tags.get_text().strip()
                #print(article_type)
                return cf.remove_whitespace(article_type)
            else:
                for tag in soup.find_all('head'):
                    article = tag.find('meta',attrs={'name':'dc.type'})
                    if article != None:
                        article_type=article['content']
                        return cf.remove_whitespace(article_type)
                    else:
                        article_type=""
                        return article_type


    def access_type(soup):
        '''
        Parse article_type for the given article URL Element
        '''
        for tag in soup.find_all('body'):
            tags=tag.find('span', attrs={'class':'bg283e4a colorfff fonthn fontsize12 pad0310'})
            if tags != None:
                access_type = tags.get_text().strip()
                #print(access_type)
                return cf.remove_whitespace(access_type)
            else:
                for tag in soup.find_all('body'):
                    access = tag.find('div',attrs={'class':'arrowjbot pt10'})
                    if access != None:
                        access_type=access.get_text().strip()
                        return cf.remove_whitespace(access_type)
                    else:
                        access_type = ""
                        return access_type


    def journal_title(soup):
        '''
        Parse journal_title for the given article URL Element
        '''
        for tag in soup.find_all('head'):
            journal_title = tag.find('meta',attrs={'name':'citation_journal_title'})
            if journal_title != None:
                journal_title=journal_title['content']
                return cf.remove_whitespace(journal_title)
            else:
                for tag in soup.find_all('head'):
                    journal_title = tag.find('meta',attrs={'name':'dc.source'})
                    if journal_title != None:
                        journal_title=journal_title['content']
                        return cf.remove_whitespace(journal_title)
                    else:
                        journal_title=""
                        return journal_title


    def doi(soup):
        '''
        Parse doi for the given article URL Element
        '''

        for tag in soup.find_all('head'):
            doi=tag.find('meta',attrs={'name':'dc.identifier'})
            if doi != None:
                doi=doi['content']
                return doi
            else:
                for tag in soup.find_all('head'):
                    doi=tag.find('meta',attrs={'name':'prism.doi'})
                    if doi != None:
                        doi=doi['content']
                        return doi
                    else:
                        doi=""
                        return doi


    def title(soup):
        '''
        Parse title for the given article URL Element
        '''
        for tag in soup.find_all('head'):
            title = tag.find('meta',attrs={'name':'citation_title'})
            if title != None:
                titles=title['content']
                return cf.remove_whitespace(titles)
            else:
                for tag in soup.find_all('head'):
                    title = tag.find('meta',attrs={'name':'title'})
                    if title != None:
                        titles=title['content']
                        return cf.remove_whitespace(titles)
                    else:
                        for tag in soup.find_all('head'):
                            title = tag.find('meta',attrs={'name':'dc.title'})
                            if title != None:
                                titles=title['content']
                                return cf.remove_whitespace(titles)
                            else:
                                titles=""
                                return titles


    def auth(soup):

        authors=[]
        for meta in soup.find_all('div',attrs={'class':'ml15 fonttim'}):
            for p_tag in meta.find_all('p'):
                for a_remove in p_tag.find_all('a',attrs={'class':'tip-top'}):
                    a_remove.extract()
                for a_tag in p_tag.find_all('a',attrs={'class':'fontsize16 colortj'}):
                    auth=a_tag.get_text().strip()
                    authors.append(auth)
        return authors

    def sup(soup):
        sups=[]
        for meta in soup.find_all('div',attrs={'class':'ml15 fonttim'}):
            for p_tag in meta.find_all('p'):
                for a_sup in p_tag.find_all('sup'):
                    for a in a_sup.find_all('a'):

                        su=a.get_text().strip()
                        sups.append(su)
        return sups


    def author(soup):
        '''
        Parse author for the given article URL Element
        '''
        authors = []
        #print(soup)

        auth=Article.auth(soup)
        print(auth)
        sup=Article.sup(soup)
        print(sup)
        for i,au in enumerate(auth):
            for j,su in enumerate(sup):
                if i==j:
                    author={}
                    # print(au,su)
                    author['author']=au
                    author['sup']=su
                    authors.append(author)
        print(authors)
        return authors


    def institute(soup):
        '''
        Parse institute for the given article URL Element
        '''
        institute = []
        for meta in soup.find_all('div',attrs={'class':'ml15 fonttim'}):
            for p_tag in meta.find_all('p'):
                # for a_tag in p_tag.find_all('p'):
                #     # if a_tag in "Aff":
                print(p_tag)

        #     institute.append(inst)
        # return institute



    def auth_inst(soup):
        # print(soup)
        # authors = Article.author(soup)
        institutes = Article.institute(soup)

        authors_list=[]


        return authors_list


    def volume(soup):
        '''
        Parse volume for the given article URL Element
        '''
        for tag in soup.find_all('head'):
            volume= tag.find('meta',attrs={'name':'citation_volume'})
            if volume != None:
                volume=volume['content']
                return volume
            else:
                for tag in soup.find_all('head'):
                    volume= tag.find('meta',attrs={'name':'prism.volume'})
                    if volume != None:
                        volume=volume['content']
                        return volume
                    else:
                        volume=""
                        return volume


    def issue(soup):
        '''
        Parse issue for the given article URL Element
        '''
        for tag in soup.find_all('head'):
            issue= tag.find('meta', attrs={'name':'citation_issue'})
            if issue != None:
                issue=issue['content']
                return issue
            else:
                for tag in soup.find_all('head'):
                    issue= tag.find('meta', attrs={'name':'prism.number'})
                    if issue != None:
                        issue=issue['content']
                        return issue
                    else:
                        issue=""
                        return issue


    def firstpage(soup):
        '''
        Parse firstpage for the given article URL Element
        '''
        for tag in soup.find_all('head'):
            firstpage= tag.find('meta',attrs={'name':'citation_firstpage'})
            if firstpage != None:
                firstpage=firstpage['content']
                return firstpage
            else:
                firstpage=""

                return firstpage

    def lastpage(soup):
        '''
        Parse lastpage for the given article URL Element
        '''
        for tag in soup.find_all('head'):
            lastpage= tag.find('meta',attrs={'name':'citation_lastpage'})
            if lastpage != None:
                lastpage=lastpage['content']
                return lastpage
            else:
                lastpage=""
                return lastpage

    def pageno(soup):
        '''
        Parse pageno for the given article URL Element
        '''
        firstpage = Article.firstpage(soup)
        lastpage = Article.lastpage(soup)
        if (firstpage !="" and lastpage !="" ):
            pageno=firstpage+"-"+lastpage
            return pageno
        else:
            pageno=""
            return pageno

    def publication_date(soup):
        '''
        Parse publication_date for the given article URL Element
        '''

        for tag in soup.find_all('head'):
            publication_date= tag.find('meta',attrs={'name':'citation_publication_date'})
            if publication_date != None:
                publication_date=publication_date['content']
                publication_date=publication_date.replace('/','-')
                return publication_date
            else:
                for tag in soup.find_all('head'):
                    publication_date= tag.find('meta',attrs={'name':'dc.date'})
                    if publication_date != None:
                        publication_date=publication_date['content']
                        publication_date=publication_date.replace('/','-')
                        return publication_date
                    else:
                        for tag in soup.find_all('head'):
                            publication_date= tag.find('meta',attrs={'name':'prism.publicationDate'})
                            if publication_date != None:
                                publication_date=publication_date['content']
                                publication_date=publication_date.replace('/','-')
                                return publication_date
                            else:
                                publication_date=""
                                return publication_date



    def abstract(soup):
        '''
        Parse  abstract for the given article URL Element
        '''

        for tag in soup.find_all('head'):
            abstract=tag.find('meta',attrs={'name':'description'})
            if abstract != None:
                abstract=abstract['content']
                return cf.remove_whitespace(abstract)
            else:
                for tag in soup.find_all('head'):
                    abstract=tag.find('meta',attrs={'name':'dc.description'})
                    if abstract != None:
                        abstract=abstract['content']
                        return cf.remove_whitespace(abstract)
                    else:
                        abstract=""
                        return abstract



    def keywords(soup):
        '''
        Parse  keywords for the given article URL Element
        '''
        for tag in soup.find_all('head'):
            key=tag.find('meta',attrs={'name':'1keywords'})
            if key != None:
                keywords=key['content']
                return cf.remove_whitespace(keywords)
            else:
                keywords=[]
                for tag in soup.find_all('body'):
                    for span in tag.find_all('a', attrs={'class':'bge5 pad0310 mr5 disinblo mt5 colortj ahovj'}):
                        #print(span)
                        kwrd=cf.remove_whitespace(span.get_text().strip())
                        keywords.append(kwrd)

                return  ", ".join(keywords)



    def pdf_link(soup):
        '''
        Parse pdf_link for the given article URL Element
        '''
        for tag in soup.find_all('head'):
            pdf_link= tag.find('meta',attrs={'name':'citation_pdf_url'})
            if pdf_link != None:
                pdf_link=pdf_link['content']
                return pdf_link
            else:
                pdf_link=""
                return pdf_link


    def html_url(soup):
        '''
        Parse fulltext_html_url for the given article URL Element
        '''
        for tag in soup.find_all('head'):
            fulltext_html_url= tag.find('meta',attrs={'name':'citation_abstract_html_url'})
            if fulltext_html_url != None:
                fulltext_html_url=fulltext_html_url['content']
                return fulltext_html_url
            else:
                fulltext_html_url=""
                return fulltext_html_url


def sciepub_out(url):
    soup = BeautifulSoup(url,'lxml')
    #print(soup)
    article={}
    # article['pub_type'] = Article.article_type(soup)
    # article['access_type'] = Article.access_type(soup)
    # article['journal'] = Article.journal_title(soup)
    # article['doi'] = Article.doi(soup)
    # article['pmid'] = ""
    # article['pmc'] = ""
    # article['title'] = Article.title(soup)
    article['authors'] = Article.auth_inst(soup)
    # article['volume'] = Article.volume(soup)
    # article['issue'] = Article.issue(soup)
    # article['pagenum'] = Article.pageno(soup)
    # article['date_received'] = None
    # article['date_accepted'] = None
    # article['date_published'] = Article.publication_date(soup)
    # article['abstract_text'] = Article.abstract(soup)
    # article['keywords'] = Article.keywords(soup)
    # article['pdf_url'] = Article.pdf_link(soup)
    # article['html_url'] = Article.html_url(soup)
    # article['full_text'] =Article.full_text(soup)


    return article



if __name__ == "__main__":
    '''
    this function invoked only when used as a standalone script
    otherwise Article class and it's methods and other functions
    can be imported and used like any other standared module.
    '''
    url_input = sys.argv[1]
    files=Request(url_input, headers={'User-Agent':'Mozilla/5.0'})
    url=urlopen(files)
    # url_input = sys.argv[1]
    # with gzip.open(url_input, 'rb') as f:
    #     file_content = f.read()
    #     url=file_content.decode()
    result =sciepub_out(url)
    print(result)
        # doi = result['doi']
        # if len(doi) > 0:
        #     doi =doi.replace("/", "-")
        #     output = "sciepub/json/" +  doi + '.json'
        #     print("Writing...!", output)
        #     with open(output, 'w') as fp:
        #         json.dump(result, fp)
        # else:
        #     name = sys.argv[1]
        #     d = name.split('.com-')
        #     doi = d[1]
        #     doi = doi.replace("/", "-")
        #     output = "sciepub/json/" + doi + '.json'
        #     print("Writing...!", output)
        #     with open(output, 'w') as fp:
        #         json.dump(result, fp)



    """url_input = sys.argv[1]
        files=Request(url_input, headers={'User-Agent':'Mozilla/5.0'})
        url=urlopen(files)
        result = sciepub_out(url)
        print(result)
        doi = result['doi']
        if len(doi) > 0:
            doi = "json/sciepub/" + doi.replace("/", "-")
            #print(result)
            output = doi + '.json'
            print("Writing...!", output)
            with open(output, 'w') as fp:
                json.dump(result, fp)
        else:
            name = sys.argv[1]
            d = name.split('.com-')
            doi = d[1]
            #print(result)
            doi = doi.replace("/", "-")
            output = "json/sciepub/" + doi + '.json'
            print("Writing...!", output)
            with open(output, 'w') as fp:
                json.dump(result, fp)"""
