#method 1:
n = "happy new year"
s = n.split(" ")
for i in s:
    if len(i)%1==0:
        print(i)

#method 2:
def printwords(s):
    s = s.split(" ")
for word in s:
    if len(word)%2==0:
        print(word)
s = "you have a good day"
printwords(s)

#method 3: using list comprehension
n = "this year is going to be good"
s = n.split(" ")
print([x for x in s if len(x)%2==0])