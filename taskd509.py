def task(t):
    res=''
    for i in t:
         res=res+str(i)+'->'
    return res[:-2]
n=list(map(int,input()[1:-1].split(",")))
print(task(n))
