def primenumber(n):
    if (n==2):
        return (n,"True")
    else:
        return(n,"False")
inp=list(map(int,input("Enter a value:").split()))
print(primenumber(inp))
