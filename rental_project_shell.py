import time, sys
import rental_project_core
import rental_project_disk

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
    details = {
        'Make': 'Chevrolet Silverado',
        'Year Model': '2013',
        'Color': 'Black',
        'Drive Train': '4wd',
        'Cabin': 'Crew Cab',
        'Engine': '6.0L Vortec Max',
        'Interior': ['Black Leather', 'Touch Screen Navigation Radio', 'Heated Seats', '5% Limo Tint All Around'],
        'Exterior Off-Road Upgrades': 'Yes',
        'Lift': '4.5 in. Suspension By Rough Country',
        'Wheels': '22 in. Monster XD',
        'Tires': 'Nitto Mud-Grappler',
        'Light': ['52 in. Creed Light-Bar "24 in. In Front Brush-Guard"', 'Halo Projector w/ 12000k Blue HID "Low&High"'],
        'Re-Enforcement': 'Ranch-Hand Brushguard ""Black" "Front&Back"'
    }
    for detail in details.items():
        print(detail[0], detail[1])

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
        details = slow_type('\n\nTo Look At The List Of Vehicles Of This Brand Press "ENTER".\n\n\n')
        list_vehicles()

        step_2 = slow_type('\n\nWhich One Of These Vehicles Suit Your Needs The Most? ')
        if step_2 == 'Chevrolet Silverado 4wd':
            slow_type('\n\nPlese Hit "ENTER" To See Details On This Vehicle...\n\n\n\n ')
            silverado(details)
            print('\n\n\n\nk')



        
            

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