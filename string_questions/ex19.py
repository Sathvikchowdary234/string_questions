#count and display vowels in a string:

# method - 1: using collections.counter with a list comprehension:
from collections import Counter 

s = "laptop is supercool!"
v = "aeiouAEIOU"
cnt = Counter([i for i in s if i in v])
print(cnt) 

# method - 2: Using str.count() :
s = "Laptop is supercool to use!"
vowels = "aeiouAEIOU"
cnt = {i: s.count(i) for i in vowels if i in s}
print(cnt)

#method - 3: Using regular expressions:
import re
s = "Python is fun!"
p = r'[aeiouAEIOU]'
vowel = re.findall(p, s)
print(f"Count: {len(vowel)}, Vowels: {vowel}")
