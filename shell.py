import time, sys
import core
import disk

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

def list_vehicles(chevrolet):
    vehicles = {'Chevrolet Silverado 4wd': 5, 'Chervolet Colorado 4wd': 4, 'Cherolet Tahoe 4wd': 3}
    for vehicle in vehicles.items():
        print (vehicle[0], vehicle[1])


def silverado(details):
    """(str) -> (str)
    Prints details for Chevrolet Silverado 4wd.
    """
    details = [
        '\nMake And Model:', 'Chevrolet Silverado',
        '\nYear Model:', '2013',
        '\nEngine:', '6.0L Vortec Max',
        '\nDrive Train:', '4WD',
        '\nFuel:', 'Gasoline',
        '\nColor:', 'Black',
        '\nCabin:', 'Crew Cab',
        '\nInterior:', 'Black Leather, Touch Screen Navigation Radio, Heated Seats, 5% Limo Tint All Around',
        '\nExterior Off-Road Upgrades:', 'Yes',
        '\nLift:', '4.5 in. Suspension By Rough Country',
        '\nWheels:', '22 in. Monster XD',
        '\nTires:', 'Nitto Mud-Grappler',
        '\nLightening:', '52 in. Creed Light-Bar "24 in. In Front Brush-Guard, Halo Projector w/ 12000k Blue HID "Low&High"',
        '\nRe-Enforcement:', 'Ranch-Hand Brushguard ""Black" "Front&Back"',
        '\nTOTAL RETAIL PRICE: ', '$43,800\n'

    ]
    for detail in details:
        print(detail)




def colorado_details(details):
    """ (str) -> (str)
    Prints details for Chevrolet Colorado 4wd.
    """
    details = [
        '\nMake And Model: Chevrolet Silverado'
        '\nYear Model: 2012'
        '\nEngine: 3.5 L Vortec'
        '\nFuel: Gasoline'
        '\nDrive Train: 4WD'
        '\nColor: Silver'
        '\nCabin: Crew Cab'
        '\nInterior: Cloth, Touch Screen Navigating Radio, Roll Cage, 5% Limo Tint All Around'
        '\nExterior Off-Road Upgrades: Yes'
        '\nLift: 5 in. Suspension by Rough Country'
        '\nWheels: 22 in. Fuel Rims "BLACK"'
        '\nTires: 33 in. Nitto Trail-Grapplers'
        '\nLightening: 45 in. Creed Lightbar "24 in. In Front Bull-Bar", 10000K HId "Low&High" w/ Spider Halo Rings'
        '\nRe-Enforcement: Roll-Cage, Rough_Country Bull-Bar, Headlight & Tail-Light Covers'
        '\nTOTAL RETAIl PRICE:  $26,400\n'
    ]

    for detail in details:
        slow_type(detail)

def tahoe(details):
                """(str) -> (str)
                Prints details for Chevrolet Tahoe 4wd.
                """
                details = [
                    '\nMake And Model: ', 'Chevrolet Colorado',
                    '\nYear Model: ', '2016',
                    '\nEngine: ', '5.3 L Vortec',
                    '\nFuel: ', 'Gasoline',
                    '\nDrive Train: ', '4WD',
                    '\nColor: ', 'Mossy Oak Vinyl',
                    '\nCabin: ', 'Crew Cab "8 Passanger"',
                    '\nInterior: ', 'Cloth, Touch Screen Navigating Radio, Dolby Surround Speakers "All Around You", Touch Screen TV/s All Around, A.C All Around',
                    '\nExterior off-Road Upgrades: ', 'Yes',
                    '\nLift: ', '3.5 Suspension By Rough Country',
                    '\nWheels: ', '24 in. Rock-Star XD "Black"',
                    '\nTires: ', '35 in. Nitto Trail Grapplers',
                    '\nLightening: ', '52 in. Creed Light-Bars "STACKED", GO-Light, Fog Lamps "HID 6000K", 32 in. LED Lightbars X2"Facing Backwards Reverse"',
                    '\nRe-Enforcement: ', 'Out-Law Winch Mount Guard "Front", Ranch-Hand Rear Tailight Guards, Wind-Shield Protector Bar',
                    '\nTOTAL RETAIL PRICE: ', '$54,200\n'
                ]
                
                for detail in details:
                    print(detail)

def list_vehicles(GMC):
    """(str) -> (str)
    Prints List 
    """ 
    vehicles = [
        '2013 GMC Sierra 1500 z71',
        '2011 GMC Sierra 2500 DuraMax z71',
        '2017 GMC Denali Super Sport z71'
    ]
    for vehicle in vehicles.items():
        print(vehicle)

print('\n\nWELCOME TO VARGAS\' VEHICLE RENTAL COMPANY FOR OFFROAD!')
time.sleep(1)

slow_type('\n\n\n\nTo Look At Our List Of Options, Please Press "ENTER"')
print_options_1()
time.sleep(1.5)

step_1 = slow_type('\n\n\nWhat Would You Like To Do Today?              \n\nPlease Enter Option Number As Provided: ')

if step_1 == '1':
    print('\n\nGreat!')
    time.sleep(.6)
    slow_type('\n\n\nPlease Hit "ENTER" To View Our Brands Available!\n\n')
    print_brands()

    brand_choice = slow_type('\n\nPlease Enter The Brand That You Are Most Interested In: ')

    if brand_choice == '1':
        slow_type('\n\nTo Look At The List Of Vehicles Of This Brand Press "ENTER".\n\n\n')
        list_vehicles(chevrolet)

        step_2 = slow_type('\n\nWhich One Of These Vehicles Suit Your Needs The Most? ')

        if step_2 == 'Chevrolet Silverado 4wd':
            slow_type('\n\nPlease Hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n')
            silverado(details)

        elif step_2 == 'Chevrolet Colorado 4wd':
            slow_type('\n\nPlease Hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n\n')
            colorado_details(details)
        
        elif step_2 == 'Chevrolet Tahoe 4wd':
            slow_type('\n\nPlease Hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n\n')       
            tahoe(details)


    elif brand_choice == '2':
        slow_type('\n\nTo Look At The List Of Vehicles Of This Brand Press "ENTER".\n\n\n ')
        list_vehicles(GMC)

        
        step_2 = slow_type('\n\nplease Hit "Enter" To Take A Look At The Details On The Chevrolelt Sierra 4WD. ')
        sierra(details)

        
            

# elif step_1 == '2':
#     #your code here


# elif step_1 == '3':
#     #your code here


# elif step_1 == '4':
#     #your code here

# elif step_1 == '5':
#     #your code here


# else:
    #your code here