##def rev(x):
##def reverse(s):
##    x=x.split()
##    res=list(map(res,s))
##    return x[::-1]
##inp=input()
##print(rev(inp))
def rev(x):
    return x[::-1]
def reverse(s):
    s=s.split()
    res=list(map(rev,s))
    return res
inp=input()
print(rev(inp))
