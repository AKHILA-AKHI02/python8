def extract_spchar(s):
    spchar=[]
    listupperAlpha=list(range(65,91,1))
    listlowerAlpha=list(range(97,123,1))
    listdigits=list(range(48,58,1))
    for i in s:
        if ord(i)not in (listupperAlpha+listlowerAlpha+listdigits):
            spchar.append(i)
    return len(spchar)
inp=input("Enter a special character:")
print(extract_spchar(inp))
