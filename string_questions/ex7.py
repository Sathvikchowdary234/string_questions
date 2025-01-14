#find the words greater than the given length K
#method - 1:
def string_k(k, str):
    string = []
    text = str.split(" ")
    for x in text:
        if len(x) > k:
            string.append(x)
    return string 
k = 3
str = "roses are red"
print(string_k(k, str))

#method - 2: using list comprehension:
sentence = "Great things are going to happen this year"
length = 4
print([word for word in sentence.split() if len(word) > length])

#method - 3: using lambda function:
S = "Great things are going to happen this year"
K = 4
s = S.split(" ")
a = list(filter(lambda x: (len(x) > K), s)) 
print(a)
