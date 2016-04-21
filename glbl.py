count=0
def counter(n):
	global count
	count+=1
	for i in range(n):
		print i,

x=raw_input("entr limit:")
n=int(x)
counter(n)
print "no of times:",count
counter(n)
print "no of times:",count
