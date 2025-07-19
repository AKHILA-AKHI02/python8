def replaceNonVowel(s):
    res=''
    for i in s:
        if i not in'aeiouAEIOU':
            res+='*'+i+'#'
        else:
                res+=i
    return res
inp=input()
print(replaceNonVowel(inp))
