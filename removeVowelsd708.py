##xyz='''practice 10 coding problem and 50 mcq for list compenhension in python'''
##
##res=[]
##for i in xyz:
##    if i not in 'AEIOUaeiou':
##        res.append(i)
##print(res)
##print(''.join(res))


def removeVowels(s):
    return ''.join([i for i in s if i not in'AEIOUaeiou'])
inp=input()
print(removeVowels(inp))
