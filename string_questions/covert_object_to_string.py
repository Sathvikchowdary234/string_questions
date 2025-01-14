# coverting object to string:
#method - 1:
Int = 23
Float = 23.0
s1 = str(Int) 
print(s1) 
print(type(s1)) 

s2= str(Float) 
print(s2) 
print(type(s2))

#example - 2: Using repr() to convert an object to a string:
print(repr({"a": 3, "b": 4})) 
print(repr([3, 4, 5])) 
class C(): 
	def __repr__(self): 
		return "This is class C"
print(repr(C()))
