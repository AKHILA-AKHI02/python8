##def removeDigits(s):
##    return ''.join([i for i in s if i not in '0123456789'])
##inp=input()
##print(removeDigits(inp))


xyz='''practice 10 coding problem and 50 mcq for list compenhension in python'''
res=[]
for i in xyz:
    if i not in '0123456789':
        res.append(i)
print(res)
print(''.join(res))
