##n=[11,8,5,21,9,11,5,11,9,21,8]
##print(n)
##new_set=set(n)
##n=list(new_set)
##print(n)


def printlist(s):
    return list(set(s))
inp=list(map(int,input().split()))
print("orginal list",inp)
print("modified list",printlist(inp))
