def create(name):
	fout=open(name,"w")
	line1=raw_input("Name:")
	fout.write(line1)
	line2=raw_input("Addr:")
	fout.write(line2)
	line3=raw_input("Age:")
	fout.write(str(line3))
	fout.close()

def show(name):
	fin=open(name,"r")
	line=fin.read()
	print line

def direct(name):
	#mkdir name
	#cd name
	x=raw_input("Entr another name:")
	create(x)

import os
print ".....................showing the file operations...................."
name=raw_input("Enter the Directory name:")
mkdir name
if os.path.isfile(name):
	show(name)
else:
	direct(name)
	show(name)


	
