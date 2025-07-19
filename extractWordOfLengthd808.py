def extractWordOfLength(s):
    s=s.split()
    res=[]
    for i in s:
        if len(i)==3:
            res.append(i)
    if len(res)==0:
        return None
    else:
        return ''.join(res)
    return res
inp=input()
print(extractWordOfLength(inp))
