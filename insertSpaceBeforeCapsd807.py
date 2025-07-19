def insertSpaceBeforeCaps(s):
    res=''
    for i in s:
        if i.isupper():
            res +=' '+i
        else:
            res+=i
    return res.strip()
inp=input()
print(insertSpaceBeforeCaps(inp))
