def rotate(s):
	x=raw_input("Enter the rotating no:")
	n=int(x)
	for i in range(len(s)):
		z=ord(s[i])
		m=z+n
		print chr(m),

a=raw_input("Enter the string:")
rotate(a)
