TICKET_PRICE = 10
tickets_remaining = 100

# O/P: How many tickets are remaining using the tickets_remaining variable.
print("There are {} ticket remaining.".format(tickets_remaining))

# Gather the user's name and assign it to a new variable.
name = input("What is your name?  ")

# Prompt the user by name and ask how many tickets they would like
num_tickets = int(input("How many tickets would you like, {}? ".format(name)))

# Calculate the price (no of ticktes multiplied by the price) and assign it to a variable.
amount_due = num_tickets * TICKET_PRICE
# O/P the price to the screen.
print("The total due is ${}".format(amount_due))
