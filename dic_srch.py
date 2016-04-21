def his(s):
	d=dict()
	for i in s:
		if i not in d:
			d[i]=1
		else:
			d[i]=d[i]+1
	return d

def search(s,x):
	c=0
	for i in s:
		if(i==x):
			c=1
			print i,":",s[i]
	if(c==0):
		print "The key",x,"is not in the string"

h=raw_input("Entr the strng:")
p=his(h)
x=raw_input("Enter the key:") 
search(p,x)

