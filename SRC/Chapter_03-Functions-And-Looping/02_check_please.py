import math


def split_check(total, number_of_people):
    """
    returns the split of check
    """
    if number_of_people <= 1:
        raise ValueError("More than 1 person is required to split the check")
    cost_per_person = total / number_of_people
    return math.ceil(cost_per_person)


print("The returned value from function is $", split_check(84.97, 4))

try:
    total_due = float(input("What is the total? "))
    number_of_people = int(input("How many people? "))
except ValueError:
    print("Oh No! That's not a valid value. Try again....")
else:
    print(
        "The returned value from function is $",
        split_check(total_due, number_of_people),
    )
