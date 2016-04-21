x=raw_input("Enter the no:")
n=int(x)
q=0
while(n!=0):
	a=n%10
	r=n*10+a
	q=a*10+q
	n=n/10
print q

