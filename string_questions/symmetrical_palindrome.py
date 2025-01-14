# symmetrical using slicing 
s = "poopoo"
half = len(s) // 2
s1 = s[:half]
s2 = s[half :] if len (s) % 2 == 0 else s [half + 1:]

if s1 ==s2:
    print(f"{s} is symmetrical")
else:
    print(f"{s} is not symmetrical")

# palindrome using slicing 
def palindrome(s):
    return s == s [::-1]

if palindrome(s):
    print("palindrome")
else:
    print("Not palindrome")

# example 2 (true or false)
def is_symmetric(s):
    return s == s[::-1]

print (is_symmetric("abba"))
print (is_symmetric("abcd"))