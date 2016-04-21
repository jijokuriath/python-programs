def circle(r):
	a=(4/3)*pi*r*r
	return a

def rect(l,b):
	a=l*b
	return a

def tri(b,h,r):
	if(b==h==r):
		a=(sqrt(3)*b**2)/4.0
		#s=(b+h+r)/2.0
		#a=sqrt(s*((s-b)*(s-h)*(s-r)))
		return (a)
	else:
		a=(1/2.0)*b*h
		return a

from math import *
k=1
while(k!=0):
	print "1) Circle\n2) Rectangle\n3) Triangle"
	x=raw_input("Entr ur choice(1-3): ")
	n=int(x)
	if(n==1):
		q=raw_input("Enter the radius of circlr:")
		r=int(q)
		a=circle(r)
		print a
	elif(n==2):
		q=raw_input("Enter the lenth:")
		l=int(q)
		p=raw_input("Enter the bredth:")
		b=int(p)
		a=rect(l,b)
		print a
	elif(n==3):
		q=raw_input("Enter the base:")
		b=int(q)
		p=raw_input("Enter the side1:")
		h=int(p)
		r=raw_input("Enter the side2:")
		i=int(r)
		a=tri(b,h,i)
		print a
	else:
		print "out of reach"
	y=raw_input("press 0 to exit:")
	k=int(y)

