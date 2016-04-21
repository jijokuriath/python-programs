def fact(n):
	if(n<=1):
		return 1
	else:
		f=n*fact(n-1)
		return f


x=raw_input(" Enter the number: ")
n=int(x)
p=fact(n) 
print "factorial of" ,n," = " ,p
	

