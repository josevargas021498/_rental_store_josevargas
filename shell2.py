import time, sys
import core2
import disk


def main():

    typing_speed = 5

    def slow_type(t):

        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(typing_speed / 970.0)
        return input()

    print('\n\nWELCOME TO VARGAS\' OFF-ROAD RENTALS!')
    time.sleep(1)

    core2.print_options_1()
    time.sleep(1)

    option = slow_type('\n\nWhat Would You Like Today? : ')

    if option == '1':
        print('\n\nSure! Here Is Our Inventory!\n\n')
        time.sleep(1)

        disk.inventory()
        time.sleep(1)

        choice = slow_type('\n\nWhat Vehicle Can I Get Your Way Today? : ')
        if choice == '1':
            vehicle = '2014 Chevrolet Silverado 1500 z71'
            weeks = slow_type(
                '\n\nHow Many Weeks Would You Like To Rent This Vehicle? : ')

            rental_cost = disk.return_rental_cost(choice)
            replacement_value = disk.return_replacement_value(choice)
            x = core2.total_cost(rental_cost, weeks, replacement_value)
            print(x)
            disk.update_history(vehicle, rental_cost, replacement_value, x)


if __name__ == '__main__':
    main()