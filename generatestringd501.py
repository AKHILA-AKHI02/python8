def generatestring(s):
    s=s.split()
    s[0]=s[0].strip()
    s[1]=s[1].strip()
    res=s[1][:2]+s[0][2:]+' '+s[0][:2]+s[1][2:]
    return res

inp=input("Enter a string:")
print(generatestring(inp))
