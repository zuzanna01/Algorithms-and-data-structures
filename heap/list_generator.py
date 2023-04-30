from random import randint

def generate_list(number_of_values, biggest_value):
    mylist = []
    for i in range(number_of_values):
        mylist.append(randint(1, biggest_value))
    return mylist


def save_list_to_csv(path, mylist):
    with open(path, 'w') as file:
        file.write(str(mylist))

