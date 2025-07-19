##def generateListDivisible():
##    return[i for i in range(900,1001) if '6'in str(i)]
##
##print(generateListDivisible())



def generateSeries():
    res=[]
    for i in range(900,1001):
        if '6' in str(i):
            res.append(i)
    return res

print(generateSeries())
