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

def print_options_1(options_1):
    options_1 = {'1.': 'Rent A Vehicle', '2.': 'Return A Vehicle', '3.': 'Look At Inventory', '4.': 'Look At Complete Inventory', '5.': 'Report Accident'}
    for option in options_1:
        print(sort(option))

print('\n\nWELCOME TO VARGAS\' VEHICLE RENTAL COMPANY FOR OFFROAD!')
time.sleep(1)
step_1 = slow_type('\n\nWhat Would You Like To Do Today?\n\nTo Look At Our List Of Options, Please Press "ENTER"')
print_options_1()