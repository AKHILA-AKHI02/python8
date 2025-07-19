##def findSmallestElement(n):  #for loop
##    nc=len(n); res=n[0]
##    for count in range (nc):
##        if res>n[count]:
##            res=n[count]
##    return res
##inp=list(map(int,input("Enter a value:").split()))
##print(findSmallestElement(inp))


def findSmallestElement(n): #min function
    return min(n)
inp=list(map(int,input("Enter a value:").split()))
print(findSmallestElement(inp))

