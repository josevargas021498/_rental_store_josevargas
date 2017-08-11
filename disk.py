def inventory():
    with open('inventory.txt', 'r') as file:
        file.readline()
        vehicles = file.readlines()
        for vehicle in vehicles:
            print('\n' + vehicle + '\n')


def return_replacement_value(input):
    """(input) -> (text)
    Returns replacement value from
    inventory.txt
    """
    with open('inventory.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        if input in line:
            pieces = line.split(', ')
            replacement_value = pieces[3].strip()
            return replacement_value


def return_price(input):
    """(input) -> (text)
    Returns price for rent from
    inventory.txt
    """
    with open('inventory.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        if input in line:
            pieces = line.split(', ')
            price = pieces[2]
            return price


def update_history(vehicle, rental_price, weeks, rental_replacement_value,
                   total_cost):
    """ (input) -> (txt)
    Updates history.txt for every transaction made.
    """
    msg = ('{}, {}, {}, {}, {}\n').format(vehicle, rental_price, weeks,
                                          rental_replacement_value, total_cost)
    with open('history.txt', 'a') as file:
        file.write(msg)


def quantity_in_inventory(input):
    """ -> (txt)
    Has quantity of vehicle.
    """
    with open('inventory.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        if input in line:
            pieces = line.split(', ')
            quantity = pieces[4]
            return quantity


def return_vehicle(str, vehicle, weeks, rental_replacement_value):
    """(input) -> (txt)
    Updates history.txt with vehicles being returned.
    """
    msg = ('{}, {}, {}, {}\n').format('RETURN', vehicle, weeks, rental_replacement_value)
    with open('history.txt', 'a') as file:
        file.write(msg)
            

def open_transaction_history_and_display():
    """_-> (list)
    Displays transaction history from history.txt
    to user.
    """
    with open('history.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
        for line in lines:
            print(line)