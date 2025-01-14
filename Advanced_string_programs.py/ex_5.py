#Avoid last occurance of delimeter:

#method - 1: using string slicing:
test_list = [5, 3, 1, 8, 4, 9, 2]
print("the original string is : " + str(test_list))
delim = "$"

res = ""
for ele in test_list:
    res += str(ele) + "$"

res = res[:len(res) -1]

print("The joined string : " + str(res) )

#method - 2: using map() + join() + str()

test_list = [3, 6, 8, 5, 1, 2, 4]
print("The original string is : " + str(test_list))
delim = "$"
res = delim.join(map(str, test_list))
print("The joined string : " + str(res))