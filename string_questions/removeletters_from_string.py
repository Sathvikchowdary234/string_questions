#example 1
s = "sathvik chowdary"
s = s.replace("k", "")
print(s)

#example 2 using list comparision
s = "sathvik chowdary"
s = "".join([c for c in s if c != "h"])
print(s)

#example 3 using filter function
s = "sathvik chowdary"
s ="".join(filter(lambda c:c != "c", s))
print(s)

#example 4 using slicing
s = "sathvik chowdary"
idx = s.find("s")
if idx != -1:
    s = s[:idx] + s[idx+1:]

print(s)