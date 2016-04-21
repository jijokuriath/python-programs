def fact(n):
	if(n<=1):
		return 1
	else:
		f=n*fact(n-1)
		return f

from math import *
x=raw_input("Entr the value of k: ")
k=int(x)
y=0
z=0
t=(2*sqrt(2))/9801
while(y!=k+1) :
	f1=4*fact(y)
	f2=fact(y)
	p=4*y
	n=(f2**4)*(396**p)
	s=(f1*(1103+(2639*y)))
	z=z+(s/float(n))
	print "k=",y
	print "f1=",f1
	print "f2=",f2
	print "p=",p
	print "s=",s
	print "n=",n
	print "s/n=",s/float(n)
	print "z=",z
	print"-------------------------"
	y=y+1
	
a=z*t
print "t=",t
print "s=",a
print "1/pi=",1/pi
