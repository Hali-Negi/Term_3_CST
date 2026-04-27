"""
---Mutable types---
Demonstrating passing mutable arguments into functions treat the parameters similar to pass by reference
until an assignment occurs in the function
"""

class NumWrapper:
    def __init__(self, num):
        self._num = num

    def add(self, num):
        self._num += num

#Pass by assignment revisited
def add_list(inner_list):
    print("Before append id(list)", id(inner_list), "Inner list:", inner_list)
    inner_list.append(3)
    print("After append id(list)", id(inner_list), "Inner list:", inner_list)
    inner_list = [] #list assigned to new object []
    print("After assignment id(list)", id(inner_list), "Inner list:", inner_list)
    inner_list.append(999) #append to local list, doesn't affect global passed in list
    print("After assignment id(list) and append", id(inner_list), "Inner list:", inner_list)

# TRY IT OUT - See if the same mutable behavior applies for the custom NumWrapper class
def add_num_wrapper(num_wrapper):
    num_wrapper.add(3)
    print("Inner num_wrapper._num:", num_wrapper._num)
    num_wrapper = NumWrapper(999) #NumWrapper assigned to new object
    num_wrapper.add(999)
    print("Inner num_wrapper._num:", num_wrapper._num)


num_wrapper = NumWrapper(0)
list = [1,2]

print("---Original values outside functions---")
print("Original list id(list)", id(list), "list:", list)
# print("num_wrapper:", num_wrapper._num)

print()
print("---Modifying values---")
add_list(list)
# add_num_wrapper(num_wrapper)

print()
print("---Final values outside functions---")
print("list:", list)
# print("num_wrapper:", num_wrapper._num)