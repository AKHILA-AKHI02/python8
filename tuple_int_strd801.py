def tuple_int_str(tuple_str):
    result=[(int(x[0]),int(x[1]))for x in tuple_str]
    return tuple(result)
tuple_str=(('333','33'),('1416','55'))
#print("Orginal tuple values:")
#print(tuple_str)
#print("\nNew tuple values:")
print(tuple_int_str(tuple_str))
