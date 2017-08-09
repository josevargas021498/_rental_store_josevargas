def print_options_1():
    """ -> (str)
    Prints out all of our options available to the user.
    """
    options_1 = [
        '\n1. Rent A Vehicle', '\n2. Return A Vehicle',
        '\n3. Look At Inventory', '\n4. Look At Completely Inventory',
        '\n5. Report An Accident'
    ]
    for option in options_1:
        print(option)


def total_cost(rental_cost, weeks, replacement_value):
    """ (int, int, float) -> (float)
    Returns the rental cost with taxes.
    """
    tax = 0.07
    deposit = 0.10

    rent_cost = rental_cost * int(weeks)
    rent_cost_w_tax = rent_cost * int(tax) + rent_cost
    dep = int(deposit) * replacement_value
    total = rent_cost_w_tax + dep
    return total
