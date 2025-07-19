def split(s):
    s=s.split()
    res=' '
    return   min(map(len,s))
inp=input("enter the length:")
print(split(inp))
