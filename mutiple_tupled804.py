def mutiple_tuple(s):
    product=1
    for x in s:
        product *=x
    return product
s=(4,3,2,2,-1,18)
#print("Orginal Tuple:")
#print(s)
#print("Product-multiplying all the numbers of the said tuple",
      #mutiple_tuple(s))
print(mutiple_tuple(s))
