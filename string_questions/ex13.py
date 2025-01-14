#split string into list of characters in python:
#method - 1: using list:
s = "Good night"
a = list(s)
print(a)

# method - 2: Using Loop:
s = "Good bye"
a = []
for char in s:
    a.append(char)
print(a)

#method - 3: using lsit comprehension:
s = "Kandimalla"
a = [ char for char in s]
print(a)

#method - 4: using unpacking operator:
s = "sweet"
a =[*s]
print(a)
