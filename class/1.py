# Person: 
# first_name 
# last_name 
# age
# birthdate 

# person1 = {
#     "first_name": "amirreza",
#     "last_name": "azimi",
#     "age": 11,
#     "birthdate": 1392
# }

# person2 = {
#     "first_name": "mohammad",
#     "last_name": "hosseini",
#     "age": 28,
#     "birthdate": 1374
# }

# print(person1['first_name'] + " " + person1['last_name'])
# print(person2['first_name'] + " " + person2['last_name'])

# DRY:   DONT REPEAT YOURSELF

# class Person1:
#     first_name= "mohammad"
#     last_name= "hosseini"
#     age= 28
#     birthdate= 1374

#     def print_fullname(self):
#         print(self.first_name + " " + self.last_name)

# class Person2:
#     first_name= "amir"
#     last_name= "hosseini"
#     age= 28
#     birthdate= 1374

#     def print_fullname(self):
#         print(self.first_name + " " + self.last_name)

# p1 = Person1()
# p1.print_fullname()

# p2 = Person2()
# p2.print_fullname()


# class Person:
#     def __init__(self, first_name, last_name, age, birthdate) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.birthdate = birthdate
    
#     def print_fullname(self):
#         print(self.first_name + " " + self.last_name)
    

# amirreza = Person(first_name="amirreza", last_name="azimi", age=11, birthdate=1392)
# amirreza.print_fullname()

# mohammad = Person(first_name="mohammad", last_name="hosseini", age=28, birthdate=1374)
# mohammad.print_fullname()

# color, max_speed, door_number, tire_number=4, brand
class Car:
    tire = 4
    def __init__(self, color, max_speed, door_number, brand) -> None:
        self.color = color
        self.max_speed = max_speed
        self.door_number = door_number
        self.brand = brand
    
    def __str__(self) -> str:
        return self.brand + " : " + self.color
    
    def push_buzzer(self):
        print("Boooogh")
    
    def car_info(self):
        # return f"Brand : {self.brand} \nColor: {self.color} \nMaxSpeed: {self.max_speed} \nDoor Number: {self.door_number}"
        return (
            f"Brand : {self.brand} \n"
            f"Color: {self.color} \n"
            f"MaxSpeed: {self.max_speed} \n"
            f"Door Number: {self.door_number}"
        )

def test():
    name = "amirreza"
    print(name)


bmw = Car(color='red', max_speed=350, door_number=2, brand='B M W')

# print(bmw)
# print(bmw.car_info())
# print("*"*50)
cheverlet = Car(color='yellow', max_speed=200, door_number=4, brand='cheverlet')
# print(cheverlet.car_info())

# print(bmw.tire)
# print(cheverlet.tire)
# print(Car.tire)

# print(Car.tire)
# print(bmw.tire)
# print(cheverlet.tire)
# bmw.push_buzzer()
# cheverlet.push_buzzer()
# print(bmw.color)
# print(cheverlet.color)

# shopping_list = ['rice', 'ice cream']
# shopping_list.append('pofak')
# print(shopping_list.index('rice'))

# print(bmw.color)

# bmw.color = 'blue'

# print(bmw.color)

print(bmw.tire)
print(cheverlet.tire)

# instance attribute
bmw.tire = 6
print("*" * 50)
print(bmw.tire)
print(cheverlet.tire)

Car.tire = 8
print("*" * 50)
print(bmw.tire)
print(cheverlet.tire)

cheverlet.tire = 10
print("*" * 50)
print(bmw.tire)
print(cheverlet.tire)

print("*" * 50)
print(Car.tire)

Car.tire = 16
print("*" * 50)
print(bmw.tire)
print(cheverlet.tire)
