def replaceAlphabetByNumber(s):
    d=dict()
    count=1
    for i in range(65,91):
        d[chr(i)]=count
        count +=1
    count=1
    for i in range(97,123):
        d[chr(i)]=count
        count +=1
    temp=''
    for i in s:
        if i.isalpha():
            temp=temp+str(d[i])+''
    return temp
inp=input()
print(replaceAlphabetByNumber(inp))
