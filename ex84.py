def find(word,letter):
	count=0
	for i in range(len(word)):
		if(word[i]==letter):
			print "The letter",letter,"is incd",i+1,"th positon"
			count=count+1
	return count
			
b=raw_input("Entr the string:")
s=raw_input("Enter the letter to find:")
c=find(b,s)
if(c==0):
	print "There is no letter",s,"in the word banana"
else:
	print "The letter",s,"is repeated in the word ",b," is",c,"times"

