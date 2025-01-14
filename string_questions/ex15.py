#convert string to a list in python:

#method -1: using split() method
s = "Its expected to snow this week"
a = s.split()
print(a)
#splitting by comma 
s = "Its expected to snow this week"
a = s.split(',')
print(a)

#method - 2: using list()
s = "Windows laptops are good"
a = list(s)
print(a)

#method -3: using list comprehension
s ="had your breakfast?"
a = [ch for ch in s]
print(a)
