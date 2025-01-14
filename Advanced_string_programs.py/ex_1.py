#convert numeric words to numbers
#Method - 1: using loop + join() + split() :
help_dict = {
    "one" : "1",
    "two" : "2",
    "three": "3",
    "four" : "4",
    "five" : "5",
    "six"  : "6",
    "seven": "7",
    "eight": "8",
    "nine" : "9",
    "zero" : "0",
}
test_str = " seven six five four"
print ("The original string is : " + test_str)
res = ''.join(help_dict[ele] for ele in test_str.split())
print("The string after performing replace : " + res)

#method - 2: using regular expressions (re):
import re
 
def convert_to_numbers(s):
   
    words_to_numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }
 
    pattern = re.compile(r'\b(' + '|'.join(words_to_numbers.keys()) + r')\b')
    return re.sub(pattern, lambda x: words_to_numbers[x.group()], s)

s = "zero five nine two one"
print(convert_to_numbers(s))
