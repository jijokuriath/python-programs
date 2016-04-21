def fibi(n):
	if(n<=1):
		return n
	else:
		return fibi(n-1)+fibi(n-2)

x=raw_input("Enter the num:")
n=int(x)
for i in range(0,n):
	print fibi(i),
	

