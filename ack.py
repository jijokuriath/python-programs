def ackman(m,n):
	if(m==0):
		print n+1
	elif ((m>0) and (n==0)):
		print m-1,1
	elif((m>0) and (n>0)):
		print m-1,m,n-1

x=raw_input("Enter m:")
m=int(x)
y=raw_input("Enter n:")
n=int(y)
ackman(m,n)



