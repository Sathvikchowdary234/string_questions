#Sort String list by K character frequency:

#method -1: using sorted() + count() + lamda :

test_list = ["Its", "time", "to", "chill"]
print("The original list is : " + str(test_list))
K = 'e'
res = sorted(test_list, key = lambda ele: -ele.count(K))
print("Sorted String : " + str(res))
