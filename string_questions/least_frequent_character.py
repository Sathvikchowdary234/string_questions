#method - 1
test_str = "Good morning everyone"
print ("The original string is : " + test_str)
all_freq = {}
for i in test_str:
 if i in all_freq:
  all_freq[i] += 1
else:
 all_freq[i] = 1
res = min(all_freq, key = all_freq.get) 
print ("The minimum of all characters in GeeksforGeeks is : " + str(res))

#method - 2:
from collections import Counter 
test_str = "the lone star state"
print ("The original string is : " + test_str)
res = Counter(test_str)
res = min(res, key = res.get) 
print ("The minimum of all characters in the lone star state is : " + str(res))

#method - 3:
def least_frequent_char(input_str):
	freq_dict = {}
	
	for char in input_str:
		freq_dict[char] = freq_dict.get(char, 0) + 1
	
	min_value = min(freq_dict.values())
	least_frequent_char = ''
	
	for key, value in freq_dict.items():
		if value == min_value:
			least_frequent_char = key
			break
	return least_frequent_char

input_str = "artificial intelligence"
print(least_frequent_char(input_str))
