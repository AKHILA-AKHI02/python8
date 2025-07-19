def returnstring(s):
    temp='Extracted numbers from a said string:['
    res=[]
    s=s.split()
    for i in s:
        if i.isdigit(): #s is a list
            res.append(int(i))
    return res
inp=input()
print(*returnstring(inp))
                
