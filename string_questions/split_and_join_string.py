#Python program to split and join a string:
#method - 1:
a = "Hey where are you going?"
words = a.split()
b = "-".join(words)
print(b)

#method - 2: using splitlines:
a = "Happy\nnew\nyear"
result = a.splitlines()
print(result)

#method - 3: using join() method:
a = ['how', 'are', 'you', 'doing']
result = " ".join(a)
print(result)