import math


def split_check(total, number_of_people):
    """
    returns the split of check
    """
    cost_per_person = total / number_of_people
    return math.ceil(cost_per_person)


print("The returned value from function is $", split_check(84.97, 4))
