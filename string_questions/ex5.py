# Given a String list, extract frequency of specific characters in the whole strings list.

#method -1:
from collections import Counter
test_list = ["Texas is a pleasent state to live"]
print("The original list : " + str(test_list))
chr_list = ['a', 's', 't']
res = {key:val for key, val in dict(Counter("".join(test_list))).items() if key in chr_list}
print("Specific Characters Frequencies : " + str(res))

#method - 2:
from collections import Counter
from itertools import chain
test_list = ["Texas is a pleasent state to live"]
print("The original list : " + str(test_list))
chr_list = ['a', 's', 't']
res = {key:val for key, val in dict(Counter(chain.from_iterable(test_list))).items() if key in chr_list}
print("Specific Characters Frequencies : " + str(res))

