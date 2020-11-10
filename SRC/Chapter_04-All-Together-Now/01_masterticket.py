TICKET_PRICE = 10
tickets_remaining = 100

# Run this code continuously.
while tickets_remaining:
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

    # Prompt the user if they want to proceed. Y/N
    should_proceed = input("Do you want to proceed with the purchase Y/N ? ")
    # if they want to proceed
    if should_proceed.lower() == "y":
        # print out the screen "SOLD!" to confirm purchase
        print("SOLD!")
        # Decrement the tickets, remaining by the no of tickets purchased.
        tickets_remaining -= num_tickets
    # Otherwise...
    else:
        # TPersonalized thank you.
        print("Thanks {} for visiting.".format(name))
# Notify the user that the ticket is sold out.
print("Sorry the ticket is sold")
