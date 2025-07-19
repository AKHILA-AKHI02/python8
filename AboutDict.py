d1={1:"One",2:"Two"}
print(d1.values())
print(d1.keys())
d1.clear()
print(d1)
d1={1:"One",2:"Two"}
d2=d1.copy()
print(id(d1))
print(id(d2))
print(d1.get(1))
print(d2.get(2))
print(d1.get("One"))
print(d1.get(33))
print(d1.items())
print(d1.keys())
print(d1)
print('After popping',d1.pop(1))
print(d1)
print(d1.pop(2))
print(d1)
print('After popping 2:',d1.pop(2))
print(d1.pop(2))
print(d1)
print('After popping 2:',d1.pop(2,100))
d1={1:"One",2:"Two"}
print(d1.popitem())
print(d1)
d1={1:"One",2:"Two"}
print(d1)
d1.get(5)
print(x)
print(d1.get(2))
print(d1)
print(d1.pop(2))
print(d1)
d1={1:"One",2:"Two"}
print(d1.pop(1))
print(d1)
d1={1:"One",2:"Two"}
a=dict(One=1,Two=2,Three=3)
print(a)


       
