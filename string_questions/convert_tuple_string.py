#python program to convert tuple to string:

#method - 1: using join():
t = ("rich", "dad", "poor", "dad")
result = " ".join(t)
print(result)

#method - 2: using with list comprehension:
t = (6, 7, 8, 'how', 'to', 'kill', 'a', 'mockingbird')
res = ' '.join(str(val) for val in t)
print(res)

#method - 3: using a loop:
t = (1, 2, 3, 'hello', 'busy', 'People')
res = ''
for val in t:
    res += str(val) + ' '
res = res.strip()
print(res)