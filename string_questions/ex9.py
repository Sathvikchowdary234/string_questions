#check if a given string is binary string or not:
# method -1: using set:
def check(string):
	p = set(string)
	s = {'0', '1'}
	if s == p or p == {'0'} or p == {'1'}:
		print("Yes")
	else:
		print("No")

if __name__ == "__main__":

	string = "101010000111"
	check(string)
	
#method - 2: using simple iteration:

def check2(string):
	t = '01'
	count = 0
	for char in string:
		if char not in t:
			count = 1
			break
		else:
			pass
	if count:
		print("No")
	else:
		print("Yes")
if __name__ == "__main__":

	string = "001021010001010"
	check2(string)

