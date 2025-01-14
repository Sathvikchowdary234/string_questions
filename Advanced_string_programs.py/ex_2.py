#String slicing in Python to Rotate a String:

#method - 1:
def rotate(input,d):
	Lfirst = input[0 : d]
	Lsecond = input[d :]
	Rfirst = input[0 : len(input)-d]
	Rsecond = input[len(input)-d : ]
	print ("Left Rotation : ", (Lsecond + Lfirst) )
	print ("Right Rotation : ", (Rsecond + Rfirst))

if __name__ == "__main__":
	input = "Happy new year"
	d=2
	rotate(input,d)
	
#method - 2:
def rotate(str1,n):
	temp = str1 + str1
	l1 = len(str1)
	l2 = len(temp)
	Lfirst = temp[n : l1+n]
	Lfirst = temp[l1-n : l2-n]

	print ("Left Rotation : ", Lfirst) 
	print ("Right Rotation : ", Lfirst )

if __name__ == "__main__":
	input = "How are you guys doing today"
	d=2
	rotate(input,d)
