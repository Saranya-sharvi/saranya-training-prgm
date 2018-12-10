article={}
   article['pub_type'] = Article.article_type(soup)
   article['access_type'] =""
   article['journal'] = Article.journal_title(soup)
   article['doi'] = Article.doi(soup)
   article['pmid'] =""
   article['pmc'] = ""
   article['title'] = Article.title(soup)
   article['authors'] = Article.auth_inst(soup)
   article['volume'] = Article.volume(soup)
   article['issue'] = Article.issue(soup)
   article['pagenum'] = Article.pageno(soup)
   article['date_received'] = Article.received_date(soup)
   article['date_accepted'] = Article.accepted_date(soup)
   article['date_published'] = Article.publication_date(soup)
   article['abstract_text'] = Article.abstract(soup)
   article['keywords'] = Article.keywords(soup)
   article['pdf_url'] = Article.pdf_link(soup)
    article['html_url'] = html



#url to parse : https://pubs.acs.org/doi/pdf/10.1021/acs.jctc.8b00280
