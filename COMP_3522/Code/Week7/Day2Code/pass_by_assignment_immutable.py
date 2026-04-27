"""
---Immutable types---
Demonstrating that passing immutable arguments into functions treat the parameters similar to pass by value
"""

# TRY IT OUT - See if the same immutable behavior applies for numbers
def add_num(num):
    num += 10
    print("Inner num:", num)

def add_string(inner_string):
    print("before appending id(inner_string)", id(inner_string), "inner_string:", inner_string)
    inner_string += "bbb"
    print("after appending id(inner_string)", id(inner_string), "inner_string:", inner_string)
    inner_string = "ccc"
    print("after assignment id(inner_string)", id(inner_string), "inner_string:", inner_string)

num = 0
string = "aaa"

print("---Original values outside functions---")
# print("num:", num)
print("string:", string)
print("id(string)", id(string), "string:", string)

print()
print("---Modifying values---")
# add_num(num)
add_string(string)

print()
print("---Final values outside functions---")
# print("num:", num)
print("id(string)", id(string), "string:", string)



x = 2
print(id(2))
print(id(x))

print( x is 2 ) #True
print (x == 2) #True