# method - 1:
test_str = "underconstruction"
print("the original string:" + test_str)
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = max(all_freq, key = all_freq.get)
print ("The maximum of all characters in underconstruction is : " + str(res))

# method - 2:

from collections import Counter
test_str = "GeeksforGeeks"
print ("The original string is : " + test_str)
res = Counter(test_str)
res = max(res, key = res.get) 
print ("The maximum of all characters in GeeksforGeeks is : " + str(res))
