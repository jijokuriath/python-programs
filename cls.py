class student(object):
	name=" None"
	addr=" None"
	grd=" D"
	def show(self):
		print "Name:",self.name
		print "Address:",self.addr
		print "Grade:",self.grd
	def get(self):
		self.name=raw_input("Entr the name:")
		self.addr=raw_input("Entr the address:")
		self.grd=raw_input("Entr the grade:")
	
ob1=student()
ob2=student()
ob1.get()
ob1.show()
ob2.get()
ob2.show()

