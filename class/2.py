
class Person:
    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def print_fullname(self):
        print(f'{self.first_name} {self.last_name}')

    def print_routine(self):
        pass

    def print_job(self):
        print(f"{self.first_name} {self.last_name} is a {self.job}")




# teacher = Person(
#     first_name='maryam',
#     last_name='ghahremani',
#     age=45,
#     job='Teacher'
# )

# doctor = Person(
#     first_name='ali',
#     last_name='rezaii',
#     age=34,
#     job='Doctor'
# )

# student = Person(
#     first_name='amirreza',
#     last_name='azimi',
#     age=11,
#     job='Student'
# )

# teacher.print_fullname()
# doctor.print_fullname()
# student.print_fullname()


# teacher.print_routine()
# doctor.print_routine()
# student.print_routine()


class Teacher(Person):
    job = "Teacher"



maryam = Teacher(
    first_name='maryam',
    last_name='ghahremani',
    age=45
)

maryam.print_job()
