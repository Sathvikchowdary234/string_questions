#method- 1
from collections import OrderedDict

def removeDupWithoutOrder(str):
      return "".join(set(str)) 
def removeDupWithOrder(str): 
    return "".join(OrderedDict.fromkeys(str)) 
if __name__ == "__main__": 
    str = "the land of lincoln"
    print ("Without Order = ",removeDupWithoutOrder(str)) 
    print ("With Order = ",removeDupWithOrder(str))

#method - 2
def removeDuplicate(str):
    s = set(str)
    s = "".join(s)
    print("Without Order:", s)  
    t = ""
    for i in str:
        if i in t:
            pass
        else:
            t = t + i      
    print("With Order:", t)
str = "this is a good start"
removeDuplicate(str)

#method - 3
import operator as op
def removeDuplicate(str):
    s = set(str)
    s = "".join(s)
    print("Without Order:", s)
    t = ""
    for i in str:
        if op.countOf(t, i) > 0:
            pass
        else:
            t = t+i
    print("With Order:", t)
str = "how are you doing"
removeDuplicate(str)