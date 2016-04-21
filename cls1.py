class bank(object):
	name=[]
	amt=0
	def srch(self):
		self.pay()		
		
	def pay(self):
		a=raw_input("Enter the amount:")
		b=int(a)
		self.amt=self.amt+b
		self.show()

	def show(self):
		print self.name
		print self.acno
		print self.amt

x=raw_input("Enter the account no:")
x=bank()
x.srch()
