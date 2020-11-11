TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100


def calculate_price(num_tickets):
    """
    It takes number of tickets and returns num_tickets * TICKET_PRICE
    """
    return (num_tickets * TICKET_PRICE) + SERVICE_CHARGE


# Run this code continuously.
while tickets_remaining:
    # O/P: How many tickets are remaining using the tickets_remaining variable.
    print("There are {} ticket remaining.".format(tickets_remaining))

    # Gather the user's name and assign it to a new variable.
    name = input("What is your name?  ")

    # Prompt the user by name and ask how many tickets they would like
    try:
        num_tickets = int(input("How many tickets would you like, {}? ".format(name)))
        # Raise a ValueError if the request is for more tickets than are available.
        if num_tickets > tickets_remaining:
            raise ValueError(
                "There are only {} tickets remaining".format(tickets_remaining)
            )
    except ValueError as ex:
        print("We ran into an issue, {}. please try again.".format(ex))
    else:
        # Calculate the price (no of ticktes multiplied by the price) and assign it to a variable.
        amount_due = calculate_price(num_tickets)
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
