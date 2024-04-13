
# def add(x, y):
#     return x+y

# add = lambda x, y: x+y

# print(add(1, 6))

# def x():
#     ...

def print_information1(first_name, last_name):
    print(first_name, last_name)

def print_information2(first_name, last_name):
    print("chetori")
    print("hello", first_name, last_name)

def print_information(first_name, last_name, print_func):
    print_func(first_name, last_name)

print_information('amirreza', 'azimi', print_information1('mohammad', 'hosseini'))
print_information('amirreza', 'azimi', print_information2)

