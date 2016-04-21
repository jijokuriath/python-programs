x=raw_input("Enter the no:")
n=int(x)
a=n
p=0
while(n!=0):
	r=(n%10)
	p=p+r**3
	n=n/10
print p
if(a==p):
	print "amstrong"
else:
	print "not amstrong"

