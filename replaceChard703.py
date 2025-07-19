def replaceChar(s):
     res=''
     for i in inp:
         if i=='a':
             res+='b'
         elif i=='b':
             res+='a'
         else:
             res+=i
     return res 
inp=input()
print(replaceChar(inp))

##
##def replaceChar(s):
##     res=''
##     for i in inp:
##         if i=='x':
##             res+='y'
##         elif i=='y':
##             res+='x'
##         else:
##             res+=i
##     return res 
##inp=input()
##print(replaceChar(inp))


