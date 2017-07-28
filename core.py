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
        print (vehicle[0], vehicle[1])


def silverado(details):
    """(str) -> (str)
    Prints details for Chevrolet Silverado 4wd.
    """
    details = [
        '\nMake:', 'Chevrolet',
        '\nMake Model:', 'Silverado',
        '\nYear Model:', '2013',
        '\nEngine:', '6.0L Vortec Max',
        '\nDrive Train:', '4WD',
        '\nFuel:', 'Gasoline',
        '\nColor:', 'Black',
        '\nCabin:', 'Crew Cab',
        '\nInterior:', ['Black Leather', 'Touch Screen Navigation Radio', 'Heated Seats', '5% Limo Tint All Around'],
        '\nExterior Off-Road Upgrades:', 'Yes',
        '\nLift:', '4.5 in. Suspension By Rough Country',
        '\nWheels:', '22 in. Monster XD',
        '\nTires:', 'Nitto Mud-Grappler',
        '\nLightening:', ['52 in. Creed Light-Bar "24 in. In Front Brush-Guard"', 'Halo Projector w/ 12000k Blue HID "Low&High"'],
        '\nRe-Enforcement:', 'Ranch-Hand Brushguard ""Black" "Front&Back"'
    ]
    for detail in details:
        print(detail)




def colorado_details(details):
    """ (str) -> (str)
    Prints details for Chevrolet Colorado 4wd.
    """
    details = [
        '\nMake:', 'Chevrolet',
        '\nMake Model:', 'Colorado',
        '\nYear Model:', '2012',
        '\nEngine:', '3.5 L Vortec',
        '\nFule:', 'Gasoline',
        '\nDrive Train:', '4WD',
        '\nColor:', 'Silver',
        '\nCabin:', 'Crew Cab',
        '\nInterior:', 'Cloth, Touch Screen Navigating Radio, Roll Cage, 5% Limo Tint All Around',
        '\nExterior Off-Road Upgrades:', 'Yes',
        '\nLift:', '5 in. Suspension by Rough Country',
        '\nWheels:', '22 in. Fuel Rims "BLACK"',
        '\nTires:', '33 in. Nitto Trail-Grapplers',
        '\nLightening:', '45 in. Creed Lightbar "24 in. In Front Bull-Bar", 10000K HId "Low&High" w/ Spider Halo Rings',
        '\nRe-Enforcement:', 'Roll-Cage, Rough_Country Bull-Bar, Headlight & Tail-Light Covers'
    ]

    for detail in details:
        print(detail)