import time

# def add(a,b):
#     return a+b


def x_operation(a,b):
    c = a + b
    c *= 2
    c -= 5
    print("operation is done")
    # return c


# result = x_operation(10, 5)
# print(result)
    
def print_something():
    print("Hi Amirreza, ")
    print("How You Doing Today?")
    # return 155

# r = print_something()
# print(r)
    

def random_sleeps():
    for i in range(5):
        print(f"sleep for {i} seconds.")
        time.sleep(i)

# random_sleeps()

# def add_numbers(a, b, c):
#     return a + b + c

# t = add_numbers(1, 9, 8)
# print(t)

def add(*args):
    s = 0
    for i in args:
        s += i
    return s

# my_list = [1, 4, 8, 15]
# t = add(*my_list)
# print(t)
        
# print(sum([1,2,3,4]))
# print(sum({1,2,3,4}))

def print_full_name(first_name, last_name="azizi"):
    print(first_name + " " + last_name)

print_full_name(
    first_name="mohammad", last_name="hosseini"
)

print_full_name(
    "hosseini", "mohammad"
)

print_full_name(
    last_name="hosseini", first_name="mohammad"
)


print_full_name("ehsan")

person = {
    "first_name": "Amirreza",
    "last_name": "Azimi"
}

print_full_name(*person) # print_full_name(first_name=person["first_name"], last_name=person["last_name"])