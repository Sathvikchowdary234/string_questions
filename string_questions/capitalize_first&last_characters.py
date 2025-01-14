#method 1:
s = " twenty twenty five"

w = s.split()
res = " ".join ([
    i[0].upper() + i[1:-1] + i[-1].upper()
    if len(i) > 1 else i.upper()
    for i in w
])
print(res)

#method 2 : using map()
s = "The lone star state"
res = ' '.join(
    map(
        lambda word: word[0].upper() + word[1:-1] + word[-1].upper()  
        if len(word) > 1 else word.upper(), 
        s.split() 
    )
)
print(res)

