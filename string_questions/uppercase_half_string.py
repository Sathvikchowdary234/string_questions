#method 1:
test_str = "This is sathvik chowdary"
print("the original string is: " + str(test_str))
half_idx = len(test_str) // 2

res = " "

for idx in range(len(test_str)):
	if idx >= half_idx:
		res += test_str[idx].upper()
	else:
		res += test_str[idx]
print("the resultant string :" + str(res))

#method 2 : using string slicing and upper()
test_str = "hi this is sathvik chowdary"
print("the original string is : " + str(test_str))
hlf_idx = len(test_str) // 2

res = test_str[:hlf_idx] + test_str[hlf_idx:].upper()
print("the resultant string is : " + str(res))
