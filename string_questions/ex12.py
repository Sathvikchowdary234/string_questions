# Swap commas and dots in a String:
# method - 1:
t = str.maketrans(',.', '.,')
s = "3, 237, 4986.0567"
res = s.translate(t)
print(res)

#method - 2: using str.replace:
s = "19, 4356, 35.678502"
s = s.replace(',', '#')
s = s.replace('.', ',')
s = s.replace('#', '.')
print(s)

#method - 3: using list comprehension:
s = "17, 9876, 3679.4" 
s = ''.join(['.' if char == ',' else ',' if char == '.' else char for char in s])
print(s)