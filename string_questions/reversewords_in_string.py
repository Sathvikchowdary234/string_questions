#example 1
def reverse_words(string):
    words = string.split() 
    reversed_words = words[::-1]  
    return ' '.join(reversed_words) 

string = input("Enter a string: ")

reversed_string = reverse_words(string)

print(f"Reversed string: {reversed_string}")

#example 2 
def reverse_words(string):
	words = string.split()
	reversed_string = ''
	for i in range(len(words)-1, -1, -1):
		reversed_string += words[i] + ' '
	return reversed_string.strip()

string = "Its so pleasent today"
reversed_string = reverse_words(string)
print(reversed_string) 
