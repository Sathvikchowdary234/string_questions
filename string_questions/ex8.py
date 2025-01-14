#Python program for removing i-th character from a string
#method - 1:
s = "Twentytwentyfive"
i = 6
res = s[:i] + s[i+1:]
print(res)

#method - 2: using for loop:
s = "Twentytwentyfive"
i = 6
res = ''
for j in range(len(s)):
    if j != i:
        res += s[j]
print(res)

#method - 3: using list comprehension
s = "Twentytwentyfive"
i = 6 
res = ''. join([s[j] for j in range(len(s)) if j !=i])
print(res)