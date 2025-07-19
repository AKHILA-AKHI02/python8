##inpl=input().split()
##res=[]
##for i in inpl:
##    if len(i)<5:
##        res.append(i)
##print(*res)



def filterWords(s,n):
    return [i for i in s if len(i)<n]
inp=input().split()
print(*filterWords(inp,5))
 
