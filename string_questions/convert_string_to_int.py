# convert string to int in python:

#method - 1: using int() function:
s = "43"
n = int(s)
print(n)

#method - 2: converting strings with different bases:
# Binary string
s = "01011"
num = int(s, 2)
print(num)

# Hexadecimal string
s = "C"
num = int(s, 14)
print(num)

#method - 3: using try and except:
s = "d,e,f"
try:
    num = int(s)
    print(num)
except ValueError:
    print("Invalid input: cannot convert to integer")