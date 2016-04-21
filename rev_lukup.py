def his(s):
	d=dict()
	for i in s:
		if i not in d:
			d[i]=1
		else:
			d[i]=d[i]+1
	return d

def look_up(s,y):
	for i in s:
		if(s[i]==y):
			return y
	raise ValueError("No error")	

h=raw_input("Entr the strng:)
p=his(h)
y=raw_input("Enter the position:")
z=look_up(p,y)
print z

