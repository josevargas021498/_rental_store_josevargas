
typing_speed = 12
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return input()

def print_options_1():
    options_1 = [ '\n1. Rent A Vehicle', '2. Return A Vehicle', '3. Look At Inventory', '4. Look At Complete Inventory', '5. Report Accident']
    for option in options_1:
        print(option)

def print_brands():
    brands = ['1. Chevrolet', '2. GMC', '3. Ford']
    for brand in brands:
        print(brand)

def list_vehicles():
    vehicles = {'Chevrolet Silverado 4wd': 5, 'Chervolet Colorado 4wd': 4, 'Cherolet Tahoe 4wd': 3}
    for vehicle in vehicles.items():
        print (vehicle[0],'\t', vehicle[1])
