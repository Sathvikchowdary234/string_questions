#Program to check if a string contains any special character:
#method - 1:
import re
def run(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')   
    if(regex.search(string) == None):
        print("String is accepted")      
    else:
        print("String is not accepted.")
if __name__ == '__main__' :
    string = "$athv!kchowd@ry" 
    run(string)

#method - 2:
import string
def check_string(s):
    for c in s:
        if c in string.punctuation:
            print("String is not accepted")
            return
    print("String is accepted")
check_string("Geeks$For$Geeks")
check_string("Geeks For Geeks") 