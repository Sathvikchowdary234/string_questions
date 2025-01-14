#Python Program to Accept the Strings Which Contains all Vowels
#method - 1
s = "happy new year"
v = "aeiou"

if all (i in s.lower() for i in v):
    print(True)
else:
    print(False)

#method - 2(using set)
s = "happie birthday to you"

v = set ("aeiou")
if v.issubset(set(s.lower())):
    print("true")
else:
    print("false")