def his(s):
	d=dict()
	for i in s:
		if i not in d:
			d[i]=1
		else:
			d[i]=d[i]+1
	return d

def show(s):
	print p

h=raw_input("Entr the strng:")
p=his(h)
show(p)

