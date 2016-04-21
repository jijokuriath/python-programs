def has_e(a):
	print a
	x=raw_input("Enter the letter u want to search:")
	count=0
	for i in  a:
		if(i==x):
			count=count+1 
			return True
	return False

fin= open("word.txt","r")
line=fin.readline()
word=line.strip()
for i in fin:
	print i,
s=has_e(line)
print s

