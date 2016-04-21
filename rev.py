x=raw_input("Enter the no:")
n=int(x)
a=n
s=0
while(n!=0):
	r=n%10
	s=s*10+r
	n=n/10
if(a==s):
	print "pallindrome"
else:
	print"not pallindrome"


