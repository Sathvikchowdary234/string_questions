#python program to check if string is empty or not:

#method - 1: using comparision operator(==):
s = ""
if s == "":
    print("The string is empty.")
else:
    print("The string is not empty.")

#method - 2: using len():
s = "Hi"
if len(s) == 0:
    print("The string is empty.")
else:
    print("The string is not empty.")

#method - 3: using the truth/false behaviour:
s = ""
if not s:
    print("The string is empty.")
else:
    print("The string is not empty.")