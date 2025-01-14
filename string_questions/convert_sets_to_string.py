#convert set to string in python:

#method - 1: using str():
s = {'a', 'b', 'c', 'd'}
print("Initially")
print("The datatype of s : " + str(type(s)))
print("Contents of s : ", s)

# convert Set to String
s = str(s)
print("\nAfter the conversion")
print("The datatype of s : " + str(type(s)))
print("Contents of s : " + s)

#method - 2: using join()
# create a set
s = {'a', 'b', 'c', 'd'}
print("Initially")
print("The datatype of s : " + str(type(s)))
print("Contents of s : ", s)

S = ', '.join(s)
print("The datatype of s : " + str(type(S)))
print("Contents of s : ", S)
