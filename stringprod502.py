def stringpro(s):
    if len(s)<3:
        return s
    elif s.endswith('ing'): #s[-3:]=='ing'
      if s.startswith('st'): #extra condition
        return s+'ly'
    else:
        return s+'ing'
inp=input()
print(stringpro(inp))
