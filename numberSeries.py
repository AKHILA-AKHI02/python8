##res=[]
##for i in range(1,101):
##    for j in range(2,10):
##        if i%j==0:
##            res.append(i)
##            break
##print(res)
##    
##ans=[i for i in range(1,101) for j in range(2,10) if i%j==0]

def numberSeries(s):
    res=[]
    for i in range(1,101):
        if(i%2==0 or i%3==0 or i%4==0 or i%5==0 or i%6==0 or i%7==0 or
           i%8==0 or i%9==0):
            ##ans=[i for i in range(1,101) for j in range(2,10) if i%j==0]

            res.append(i)
    return res
inp=(input().split())
print(numberSeries(inp))


