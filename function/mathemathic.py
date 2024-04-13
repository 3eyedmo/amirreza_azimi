def add(first_number, second_number):
    return first_number + second_number


def mul(first_number, second_number):
    result = first_number * second_number
    return result

def operator(first_number, second_number, type="add"):
    if type == "mul":
        return first_number * second_number
    elif type == "add":
        return first_number + second_number
    else:
        print("please type mul or add.")
