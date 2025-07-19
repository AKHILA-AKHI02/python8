def checkAnagram(s1,s2):
    if sorted (s1)==sorted(s2):
        return'Anagram'
    else:
        return 'Not anagram'
inp=input("Enter the string:").split()
print(checkAnagram(inp[0],inp[1]))
