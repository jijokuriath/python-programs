def is_sort(a):
	for j in range(len(a)):
		for i in range(1,len(a)):
			if(a[i]>a[j]):
				a[]=j
				
	print a
		
p=raw_input("Enter the string or nos:")
print p
is_sort(p)


