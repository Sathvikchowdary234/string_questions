#program to find uncommon words from two Strings
#method - 1:
def UncommonWords(A, B):
    count = {}
    for word in A.split():
        count[word] = count.get(word, 0) + 1 
    for word in B.split():
        count[word] = count.get(word, 0) + 1
    return [word for word in count if count[word] == 1]
A = "Happy new year"
B = "Wishing you all a happy new year"
 
print(UncommonWords(A, B))

#method - 2:

def UncommonWords(A, B):
	A=A.split()
	B=B.split()
	x=[]
	for i in A:
		if i not in B:
			x.append(i)
	for i in B:
		if i not in A:
			x.append(i)
	x=list(set(x))
	return x
A = "Happy new year"
B = "Wishing you all a happy new year"
print(UncommonWords(A, B))
