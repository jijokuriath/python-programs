pre="JKLMNOPQ"
suf="ack"
for i in pre:
	s= i+suf
	if(s=="Oack" ):
		print "Ouack"
	elif(s=="Qack" ):
		print "Quack"
	else:
		print s
