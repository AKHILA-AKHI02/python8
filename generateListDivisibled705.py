#by using function:
##def generateListDivisible(s):
##    ans=[]
##    for i  in range(1,s+1):
##        if i%8==0:
##           ans.append(i)
##    return ans
##inp=int(input(),10)
##print(generateListDivisible(inp))


#list comprehension:
def generateListDivisible(n):
    return[i for i in range(1,n+1) if i%8==0]
inp=int(input())
print(generateListDivisible(inp))
