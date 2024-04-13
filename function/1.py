person1 = {
    "name": "amirreza",
    "age": 10
}


# name -----> amirreza
# age  -----> 10

# print(f"name -----> {person1.get('name')}")
# print(f"age  -----> {person1.get('age')}")
# print(" -------------------------------------------- ")

person2 = {
    "name": "mohammad",
    "age": 28
}

# print(f"name -----> {person2.get('name')}")
# print(f"age  -----> {person2.get('age')}")
# print(" -------------------------------------------- ")

def print_person(person):
    print(f"name -----> {person.get('name')}")
    print(f"age  -----> {person.get('age')}")
    print(" -------------------------------------------- ")


print_person(person=person1)
print_person(person=person2)