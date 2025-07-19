def duplicateCount(s):
    res=''
    for i in s:
        if s.count(i)==1:
            res+=i
    return res
inp=input()
print(duplicateCount(inp))
