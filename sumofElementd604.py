
##def sumElements(n):
##    nc=len(n);   res=0
##    for i in range(nc):
##        res +=n[i]
##    return res
##inp=list(map(int,input().split()))
##print(sumElements(inp))



##def sumElements(n):
##    return sum(n)
##inp=list(map(int,input().split()))
##print(sumElements(inp))

##def sumElements(n):
##    res=0
##    for i in n:
##        res+=i
##    return res
##inp=list(map(int,input().split()))
##print(sumElements(inp))


def sumElements(n):
    nc=len(n);   i=0;   res=0
    while(i<nc):
        res +=n[i]
        i+=1
    return res
inp=list(map(int,input().split()))
print(sumElements(inp))



