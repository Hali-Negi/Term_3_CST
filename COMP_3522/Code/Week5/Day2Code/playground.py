def my_function():
    print("Hi")

function_list = [my_function] * 3
for func in function_list:
    func()