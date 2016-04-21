def rev(a):
	l=len(a)+1
	p=[]
	for i in range(-1,-l,-1):
		p.append(a[i])
	print p
	print a

x=raw_input("Entr the list:")
rev(x)


