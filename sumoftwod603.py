def sum_of_two(nx):
    n=int(input("Enter no of element in a list:"))
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    nx=[]
    for i in range(0,n,1):
        nx.append(arr1[i]+arr2[i])
    return nx
nx=(input())
print(sum_of_two(nx))

##n=int(input("Enter No Of Element in a list:"))
##arr1 =list(map(int, input().split()))
##arr2 =list(map(int, input().split()))
##na=[]
##for i in range(0,n,1):
##    na.append(arr1[i]+arr2[i])
##print(na)
##    
