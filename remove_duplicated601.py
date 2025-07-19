def remove_duplicate(x):
    nx=[]
    for i in x:
        if i not in nx:
            nx.append(i)
    return nx
inp=list(map(int,input("Enter:").split(",")))
print(remove_duplicate(inp))


##x=[11,8,5,21,9,11,5,11,9,21,8]
##print(x)
##nx=[]
##for i in x:
##    if i not in nx:
##        nx.append(i)
##print(nx)
