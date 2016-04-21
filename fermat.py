def check(a,b,c,n):
	a=a**n
	b=b**n
	c=c**n
	if(a+b==c):
		print a,"+",b,"=",c
		print "Holy smokes, Fermant was wrong" 
	else:
		print "Not work"


x=raw_input(" Enter the a: ")
a=int(x)
y=raw_input(" Enter the b: ")
b=int(y)
z=raw_input(" Enter the c: ")
c=int(z)
p=raw_input(" Enter the n: ")
n=int(p)
if(n>2):
	check(a,b,c,n)
else:
	print  "No that doesn't work"



	
