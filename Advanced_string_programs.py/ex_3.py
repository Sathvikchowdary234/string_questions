# Check if a string can become empty by recursive deletion using Slicing:

def can_become_empty_with_slicing(string, substring):
    if not string:
        return True
    
    index = string.find(substring)
    if index != -1:
        return can_become_empty_with_slicing(string[:index] + string[index + len(substring):], substring)
    return False

input_string = "sathvikchowdary"
substring = "geeks"
result = can_become_empty_with_slicing(input_string, substring)

print(result)
