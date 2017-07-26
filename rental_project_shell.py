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

    brand_choice = slow_type('\n\n1Please Enter The Brand That You Are Most Interested In: ')

    # if brand_choice == '1':
        #your code here
        

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