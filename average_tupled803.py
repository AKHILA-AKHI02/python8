def average_tuple(n):
    result=[sum(x)/len(x) for x in n]
    return result
n=((10,10,10,12),(30,45,56,45),(81,80,39,32),(1,2,3,4))
print(average_tuple(n))



##def average_tuple(n):
##    result=[sum(x)/len(x) for x in n]
##    return result
##n=((1,1,-5),(30,-15,56),(81,-60,-39),(-10,2,3))
##print(average_tuple(n))
