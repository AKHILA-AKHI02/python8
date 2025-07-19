def findandreplace(s):
    x=s.find('not')
    y=s.find('poor')
    if x!=-1 and y!=-1 and x<y:
        s.replace(s[s.find('not'):s.find('poor')+4],'good')
        return s.replace(s[x:y+4],'good')
    else:
        return s
inp=input("enter:")
print(findandreplace(inp))
