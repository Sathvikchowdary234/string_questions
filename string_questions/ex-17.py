#how to sort a list of strings in python:

# method - 1 :using sort() method:
a = ["sathvik", "chowdary", "kandimalla"]
a.sort()
print(a)

#method - 2 : using sorted() function:
a = ["kandimalla", "sathvik", "chowdary"]
res = sorted(a)
print(res)

#method - 3 : using reverse order:
a = ["illinois", "iowa", "idaho"]
res = sorted(a, reverse=True)
print(res)

#method - 4 : sorting by string length:
a = ["california", "connecticut", "chicago"]
res = sorted(a, key=len)
print(res)

#method - 5 : using custom key:
a = ["florida", "newyork", "arizona", "utah"]
res = sorted(a, key=lambda s: s[-1])
print(res)