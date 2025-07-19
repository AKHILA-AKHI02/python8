def count_constant(s):
    constant=0
    for i in s:
        if i in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrtsvwyz':
            constant+=1
    return constant
str1=input("Enter the constant:")
a=count_constant(str1)
print("No of constant in:",str1,"is",a)
