def print_options_1():
    """ -> (str)
    Prints out all of our options available to the user.
    """
    options_1 = [
        '\n1.Rent-A-Vehicle',
        '\n2.Return-A-Vehicle',
        '\n3.View-Transaction-History'
    ]
    for option in options_1:
        print(option)


def total_rental_cost(rental_price, weeks, replacement_cost):
    """(para) -> (float)
    Returns Total for the rent of a
    vehicle from my company.
    """
    tax = 0.07
    deposit = 0.10

    cost_wo_tax = int(rental_price) * int(weeks)
    cost_w_tax = int(cost_wo_tax) * float(tax) + cost_wo_tax
    depos = int(replacement_cost) * float(deposit)
    total = cost_w_tax + depos
    return total


