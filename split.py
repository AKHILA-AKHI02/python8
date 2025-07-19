def split(s):
    s=s.split()
    res=' '
    return   max(map(len,s))
inp=input("enter the length:")
print(split(inp))
