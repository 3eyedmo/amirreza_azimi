
# username = input("Enter Your name:  ")
# password = input("Enter Your password:  ")

# is_correct = True

# if len(username) > 40:
#     print("username is more than 40 chars..")
#     is_correct = False
# elif len(username) < 8:
#     print("username is less than 8 chars.")
#     is_correct = False

# if len(password) > 40:
#     print("password is more than 40 chars..")
#     is_correct = False
# elif len(password) < 8:
#     print("password is less than 8 chars.")
#     is_correct = False

# if is_correct:
#     print("username and password is correct.")
# else:
#     print("username or password are not correct")


students = [
    {"name": "ali", "age": 8},
    {"name": "amirreza", "age": 10},
    {"name": "mohammad", "age": 9},
    {"name": "reza", "age": 7},
    {"name": "ehsan", "age": 6},
]

# for student in students:
#     print(student)

# person = {"name": "ehsan", "age": 6}


# numbers = [2,7,4,3]
# for number in numbers:
#     print(number)

student = {"name": "ali", "age": 8}

if student['age'] < 10:
    if student["name"].startswith('a'):
        print("shoma mitoonid sabtena konid")
