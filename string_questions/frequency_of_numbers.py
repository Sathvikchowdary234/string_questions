#method - 1:
import re
test_str = "mcdonalds is worlds no.1 brand 4 burger "
print("The original string is :" + test_str)
res = len(re.findall(r'\d+', test_str))
print("count of numerics in string : " + str(res))

#method - 2: using isdigit() method:

test_str = "mcdonalds is worlds no.1 brand 4 burger"
print("The original string is : " + test_str)
res=0
for i in test_str:
	if(i.isdigit()):
		res+=1
		
print("Count of numerics in string : " + str(res))

