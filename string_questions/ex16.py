#Convert a list of characters into a string – Python

#method - 1: using join() method:
a = ['h', 'a', 'n', 'd', 's', 'o', 'm', 'e']
s = ''.join(a)
print(s)

#method - 2: using for loop:
a = ['h', 'e', 'l', 'l', 'o']
s = ''
for c in a:
    s += c
print(s)