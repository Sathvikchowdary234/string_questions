#Python program to count number of vowels using sets in given string
#method - 1
string = "hello goodmorning"
vowels = "aeiouAEIOU"
count = sum(string.count(vowel) for vowel in vowels)
print(count)

#method - 2 (using list comprehension)
def vowel_count(str):
	vowels = "aeiouAEIOU"
	count = len([char for char in str if char in vowels])
	print("No. of vowels :", count)
str = "GeeksforGeeks"
vowel_count(str)

#method - 3 (using regex expression)
import re
string = "we're going to have snow fall today"
vowels = r"[aeiouAEIOU]"
count = len(re.findall(vowels, string))
print(count)

