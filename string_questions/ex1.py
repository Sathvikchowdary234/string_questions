#check if a string has one letter and one number
#method- 1
import re
s =  "year2025"
l = bool(re.search(r"[a-zA-Z]", s))
n = bool(re.search(r'\d', s)) 

if l and n:
    print(True)
else:
    print(False)

#method - 2 (built in string methods like set.isdisjoint())

s = "year2025"
letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTUVXYZ")
numbers = set("0123456789")

char = set(s)
print(not char.isdisjoint(letters) and char.isdisjoint(numbers))

#
def has_letter_and_number(s):
    has_letter = any(char.isalpha() for char in s)
    has_number = any(char.isdigit() for char in s)
    return has_letter and has_number

input_string = "Hello123"
if has_letter_and_number(input_string):
    print(f"The string '{input_string}' has at least one letter and one number.")
else:
    print(f"The string '{input_string}' does not have both a letter and a number.")



