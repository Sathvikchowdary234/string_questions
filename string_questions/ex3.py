# count the number of matching charaters in a pair of string
#method-1
s1 = "context"
s2 = "constant"
res = len(set(s1.lower()).intersection(set(s2.lower())))
print(res)

#method-2 (using counter)
from collections import Counter
s1 = "VISHAKSHI"
s2 = "VANSHIKA"
c1 = Counter(s1.lower())
c2= Counter(s2.lower())
res = sum((c1 & c2).values())
print(res)

#method-3 (using list comprehension)
s1 = "resistance"
s2 = "resonance"
res = len([char for char in set(s1.lower())
           if char in set(s2.lower())])
print(res)