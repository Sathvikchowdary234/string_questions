# Find all close matches of input string from a list
# method - 1: using startswith:
s = ["elephant", "ele", "dinosur", "dino"]
a = "elephant"
for string in s:
    if string.startswith(a) or a.startswith(string):
        print (string, end =" ")

#method - 2: using string slicing:
s = ["elephant", "ele", "dinosur", "dino"]
a = "elephant"
for string in s:
    if string[:len(a)] == a or a[:len(string)] == string:
        print(string, end=" ")