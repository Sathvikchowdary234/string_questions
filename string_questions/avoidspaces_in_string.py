#example - 1
string = input("enter a string: ")
length_without_spaces = sum(1 for char in string if char != " ")
print(f"the length of the string without spaces is {length_without_spaces}")

#example - 2
test_str = "learning python is fun"
print("the original string is :" + str(test_str))
res = sum(not chr. isspace () for chr in test_str)
print("the characters frequency avoiding spaces: " + str(res))

#example - 3
test_str = 'wishing you all a happy new year'
print("The original string is : " + str(test_str))
res = len(''.join([char for char in test_str if char != ' ']))
print("The Characters Frequency avoiding spaces : " + str(res))
