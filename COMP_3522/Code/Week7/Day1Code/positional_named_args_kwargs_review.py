#-------------------------***Positional arguments:***"------------------------
print("***Using positional arguments:***")

def my_regular_function(num, string, dictionary):
    print(f'num: {num}, string: {string}')
    print(f'dictionary: {dictionary}')
    print()
    for x, y in dictionary.items():
        print(f'key: {x}, value: {y}')


my_regular_function(7, "Whoa", {'my_float': 5.5, 'a_list': [4, 57], 'a_tuple': ('hi', 'bye')})


#-------------------------***Arguments list:***------------------------
print("\n", "***Using arguments list:***")

# Arguments list is great for varying number of positional arguments
def my_args_function(num, string, *args):
    print(f'num: {num}, string: {string}')
    print()
    #treat args like a list
    for item in args:
        print(f'item: {item}')

my_args_function(7, "Whoa", "What's this?", 65, {'my_float': 5.5, 'a_list': [4, 57], 'a_tuple': ('hi', 'bye')}, 4343, "fdfdf", 9.9)



# -------------------------***Named arguments:***"------------------------
print("\n", "***Using named arguments:***")

def my_named_args_function(num, string, dictionary):
    print(f'num: {num}, string: {string}')
    print(f'dictionary: {dictionary}')
    print()
    for x, y in dictionary.items():
        print(f'key: {x}, value: {y}')

my_named_args_function(dictionary = {'my_float': 5.5, 'a_list': [4, 57], 'a_tuple': ('hi', 'bye')}, string="Whoa", num=7)




#-------------------------***Keyword arguments:***------------------------
print("\n", "***Using keyword arguments:***")

# Kwargs is great for varying number of named arguments
def my_kwargs_function(num, string, **kwargs):
    print(f'num: {num}, string: {string}')
    print(f'kwargs: {kwargs}')
    print()
    #treat kwargs like a dictionary
    for x, y in kwargs.items():
        print(f'key: {x}, value: {y}')


my_kwargs_function(string="Whoa", num=7, my_float=5.5, a_list=[4, 57], a_tuple=('hi', 'bye'))
