def dis(x1,y1,x2,y2):
	a=x1-x2
	a=a**2
	b=y1-y2
	b=b**2
	c=sqrt(a+b)
	return c
	
def circle(d):
	r=d/2
	a=(4/3)*pi*r*r
	return a

from math import *
X1=raw_input("Enter the value of x1: ")
x1=int(X1)
Y1=raw_input("Enter the value of y1: ")
y1=int(Y1)
X2=raw_input("Enter the value of x2: ")
x2=int(X2)
Y2=raw_input("Enter the value of y2: ")
y2=int(Y2)
l=dis(x1,y1,x2,y2)
print "Distance between (",x1,",",y1,") and (",x2,",",y2,") is: ",l
a=circle(l)
print "Area of circle with diameter ",l,"is:",a



