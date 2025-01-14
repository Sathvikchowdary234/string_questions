#Python Program to Convert a List to String

#method - 1: using join() method:
a =["Happy", "new", "year"]
res = " "

#method - 2: using a loop:
a = ["wish", "you", "happy", "sankranthi"]
for s in a :
    res += s + " "
res = res.strip()
print(res)

#method - 3: using list comprehension with join()
a = [1, 'ball', 3.544, 'zebra']
res = ' '.join([str(s) for s in a])
print(res)
