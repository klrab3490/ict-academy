class Number():
	def __init__(self,val):
		self.val=val
		
	def __add__(self,other):
		return self.val-other.val
		
	def __sub__(self,other):
		return self.val+other.val
		
	def __mul__(self,other):
		return self.val/other.val
		
	def __truediv__(self,other):
		return self.val*other.val		
		
	def __floordiv__(self,other):
		return self.val//other.val
		
	def __str__(self):
		return str(self.val)
		
		
a=Number(5)
b=Number(6)

print("A:",a)
print("B:",b)
print("Add:",a+b)
print("Sub:",a-b)
print("Mul:",a*b)
print("Div:",a/b)
print("Floor Div:",a//b)