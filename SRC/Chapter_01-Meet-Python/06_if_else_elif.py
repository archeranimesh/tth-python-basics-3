first_name = input("What is your first name? ")
print("Hello,", first_name)
if (
    first_name == "animesh"
):  # : opens the body of the if statement, body is statements seperated by tabs
    print(first_name, "is learning Python")  # runs when expression is true.
elif first_name == "rakesh":  # anothe condition to check.
    print(first_name, "is learning with fellow students in the Community! Me too!")
else:  # executes when the if is false.
    # this is to check if younger people.
    age = int(input("How old are you? "))
    if age <= 6:
        print(
            "Wow you're {}: if you're confident with your reading already...".format(
                age  # format coerces the integer to be a string.
            )
        )
    print("You should totally learn Python, {}!".format(first_name))
print("Have a great day {}!".format(first_name))

# double equal for equality
fruit = "apples"
print(fruit == "apples")
