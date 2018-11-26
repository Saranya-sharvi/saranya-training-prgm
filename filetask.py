import json
import os
import sys
import os.path
import pwd
import time





def file_info(filename):
	fp = open(filename)
	st = os.fstat(fp.fileno())
	#fp = open("task.py")
	#st = os.fstat(fp.fileno())

	word = os.path.basename(filename)
	print(word)
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

	#print(x)
	return x
	#excpgm = sys.argv[1]
	#s=os.path.abspath(excpgm)


	#print("Path of the folder is:"+s)




path = sys.argv[1]

file_name_list = []

for file in os.listdir(path):
	if os.path.isfile(os.path.join(path, file)):
		found = os.path.join(path, file)
		out = file_info(found)
		file_name_list.append(out)
		#yield file


with open('fileoper.json', 'w')as filetask:
	json.dump(file_name_list, filetask) 

#print(file_name_list)		
		
#for file in files("."):
#	print(file)
"""for root, dirs, files in os.walk("../saranya-training-prgm"):  
	print(root)
	for filename in files:
	   	print(filename)
	   	s=os.path.abspath(filename)
	   	print(s)
	   	out = file_info(s)
	   	print(out)"""
