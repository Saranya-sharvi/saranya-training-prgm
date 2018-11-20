import json
import os
import sys
import os.path
import pwd
import time

#fp = open(sys.argv[1])

#st = os.fstat(fp.fileno())

fp = open("task.py")
st = os.fstat(fp.fileno())


word = str(sys.argv[0])
text = word.split('.')

ctm = time.ctime(st.st_ctime)
atm = time.ctime(st.st_atime)
mtm = time.ctime(st.st_mtime)
mem = (os.fstat(fp.fileno()).st_size)
path =  os.getcwd()
current_folder_name = os.path.split(os.getcwd())

x={}

try:
	userinfo = pwd.getpwuid(st.st_uid)
except(ImportError, KeyError):
	print("failed to get the owner name for", file)
else:
	x['owner_of_thefile']=userinfo.pw_name



x['filename']=fp.name
x['type_of_file']="." + text[1]
x['size_of_file']=mem
x['create _filetime']=ctm
x['access_filetime']=atm
x['modified_filetime']=mtm
x['path_of_thefile']=path
x['folder_of_thefile']=current_folder_name[1] 

with open('fileoper.json', 'w')as filetask:
	json.dump(x, filetask) 


print(x)





	
	















