print(id(2.5))
a = 2.5
type(a)
print(id(a)) # same address as id(2.5)!
a = a + 0.0456
print(id(a)) # Not the same – a contains the address of a new float!
print(id(2.5456)) 