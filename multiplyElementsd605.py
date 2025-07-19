def multiplyElements(n): #for loop
    nc=len(n);    res=1
    for i in range(nc):
        res *=n[i]
    return res
inp=list(map(int,input().split()))
print(multiplyElements(inp))
    



##def multiplyElements(n): #for each
##    res=1
##    for i in n:
##       res *=i
##    return res
##inp=list(map(int,input().split()))
##print(multiplyElements(inp))
