def string(s):
    if len(s)<3:
        return s
        if(s.endswith('ing')):
            return s+'ly'
    else:
           return s+'ing'
    
inp=input("Enter a string:")
print(string(inp))
