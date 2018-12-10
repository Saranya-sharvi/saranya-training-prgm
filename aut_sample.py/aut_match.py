from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
import re
url="https://www.omicsonline.org/open-access/typology-use-and-process-of-cola-nut-cola-nitida-produced-in-cote-divoire-2329-8863-1000379-104247.html"
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
file=requests.get(url,headers=agent)
soup=BeautifulSoup(file.content,'lxml')
object={}
second_object={}
third_object={}
array=[]
meta_data=soup.find("dl",attrs={"class":"authors"})
data=(meta_data.find("dt"))
checking=(data.find_all("a"))
# print(len(checking))
if len(checking) <= 2:
    checking_dd=meta_data.find("dd").get_text()
    object[data.get_text()]=checking_dd
    print(object)
# sample_dd=meta_data.find("dd")
# print(sample_dd)
# sample=data.get_text().split(",")
# print(sample)
# if len(sample) <= 1:
#     third_object[data.get_text()]=sample_dd.get_text()
#     print(third_object)
else:
    main=(data.select('a[href]'))
    # print(len(main))
    main_to_string=str(main)
    elt=main_to_string.split('<a href="https:')
    # print(elt[1:])
    row=elt[1:]
    for line in row:
        main=line.replace('//www','<a href="https:').replace("</a>]","</a>")
        soup_2=BeautifulSoup(main,"lxml")
        # print(soup_2)
        array.append(soup_2.get_text())
    # if len(array) <= 1:
    #     dt=(soup_2.get_text().split(","))
    #     print(dt)
    #     dd=meta_data.find("dd")
    #     dd_final=dd.get_text()
    #     third_object[dt[0]]=dd_final
    #     print(third_object)
    # else:
for ar in array:
    # print(type(ar))
    volume=(ar.split(","))
    # print(volume)
    for vol in volume:
        if vol == "*" or vol == " ":
            # print(vol)
            volume.pop()
    object[volume[0]]=volume[1:]
print(object)
institute=meta_data.find_all("dd")
# print(institute)
for insti in institute:
    answer=(insti.get_text())
    # print(type(answer))
    second_object[answer[0]]=answer[1:]
print(second_object)
