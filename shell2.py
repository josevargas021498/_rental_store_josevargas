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

    print('\n\nWELCOME TO VARGAS\' OFF-ROAD RENTALS!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
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
            vehicle_quantity = slow_type('\n\nHow Many ' + vehicle + ' Vehicles Would You Like To Rent From Us? ')
            weeks = slow_type('\n\nHow Many Weeks Would You Like To Rent This Vehicle? ')


            rental_price = disk.return_price(choice)

            rental_replacement_value = disk.return_replacement_value(choice)

            total_cost = core2.total_rental_cost(rental_price, weeks, rental_replacement_value)

            disk.update_history(vehicle, rental_price, weeks, rental_replacement_value, total_cost)


            print('\n\nCalculating Your Total Price...\n\n')
            time.sleep(1.3)
            print('\n\n\nThank You! Your Total Price Is $' + str(total_cost))
        elif choice == '2':
            vehicle = '2013 Chevrolet Colorado z71'
            vehicle_quantity = slow_type('\n\nHow Many ' + vehicle + ' Vehicles Would You Like To Rent From Us? ')
            weeks = slow_type('\n\nHow Many Weeks Would You Like To Rent This Vehicle? ')


            rental_price = disk.return_price(choice)

            rental_replacement_value = disk.return_replacement_value(choice)

            total_cost = core2.total_rental_cost(rental_price, weeks, rental_replacement_value)

            disk.update_history(vehicle, rental_price, weeks, rental_replacement_value, total_cost)


            print('\n\nCalculating Your Total Price...\n\n')
            time.sleep(1.3)
            print('\n\n\nThank You! Your Total Price Is $' + str(total_cost))

        elif choice == '3':
            vehicle = '2015 Chevrolet Tahoe 1500 z71'
            vehicle_quantity = slow_type('\n\nHow Many ' + vehicle + ' Vehicles Would You Like To Rent From Us? ')
            weeks = slow_type('\n\nHow Many Weeks Would You Like To Rent This Vehicle? ')


            rental_price = disk.return_price(choice)

            rental_replacement_value = disk.return_replacement_value(choice)

            total_cost = core2.total_rental_cost(rental_price, weeks, rental_replacement_value)

            disk.update_history(vehicle, rental_price, weeks, rental_replacement_value, total_cost)


            print('\n\nCalculating Your Total Price...\n\n')
            time.sleep(1.3)
            print('\n\n\nThank You! Your Total Price Is $' + str(total_cost))

        elif choice == '4':
            vehicle = '2007 Chevrolet Silverado DuraMax 2500 HD Unique Edition'
            vehicle_quantity = slow_type('\n\nHow Many ' + vehicle + ' Vehicles Would You Like To Rent From Us? ')
            weeks = slow_type('\n\nHow Many Weeks Would You Like To Rent This Vehicle? ')


            rental_price = disk.return_price(choice)

            rental_replacement_value = disk.return_replacement_value(choice)

            total_cost = core2.total_rental_cost(rental_price, weeks, rental_replacement_value)

            disk.update_history(vehicle, rental_price, weeks, rental_replacement_value, total_cost)


            print('\n\nCalculating Your Total Price...\n\n')
            time.sleep(1.3)
            print('\n\n\nThank You! Your Total Price Is $' + str(total_cost))

        elif choice == '5':
            vehicle = '2013 GMC Sierra 1500 z71'
            vehicle_quantity = slow_type('\n\nHow Many ' + vehicle + ' Vehicles Would You Like To Rent From Us? ')
            weeks = slow_type('\n\nHow Many Weeks Would You Like To Rent This Vehicle? ')


            rental_price = disk.return_price(choice)

            rental_replacement_value = disk.return_replacement_value(choice)

            total_cost = core2.total_rental_cost(rental_price, weeks, rental_replacement_value)

            disk.update_history(vehicle, rental_price, weeks, rental_replacement_value, total_cost)


            print('\n\nCalculating Your Total Price...\n\n')
            time.sleep(1.3)
            print('\n\n\nThank You! Your Total Price Is $' + str(total_cost))

        elif choice == '6':
            vehicle = '2011 GMC Sierra 2500 DuraMax HD z71'
            vehicle_quantity = slow_type('\n\nHow Many ' + vehicle + ' Vehicles Would You Like To Rent From Us? ')
            weeks = slow_type('\n\nHow Many Weeks Would You Like To Rent This Vehicle? ')


            rental_price = disk.return_price(choice)

            rental_replacement_value = disk.return_replacement_value(choice)

            total_cost = core2.total_rental_cost(rental_price, weeks, rental_replacement_value)

            disk.update_history(vehicle, rental_price, weeks, rental_replacement_value, total_cost)


            print('\n\nCalculating Your Total Price...\n\n')
            time.sleep(1.3)
            print('\n\n\nThank You! Your Total Price Is $' + str(total_cost))

        elif choice == '7':
            vehicle = '2017 GMC Yukon Denali High Country z71'
            vehicle_quantity = slow_type('\n\nHow Many ' + vehicle + ' Vehicles Would You Like To Rent From Us? ')
            weeks = slow_type('\n\nHow Many Weeks Would You Like To Rent This Vehicle? ')


            rental_price = disk.return_price(choice)

            rental_replacement_value = disk.return_replacement_value(choice)

            total_cost = core2.total_rental_cost(rental_price, weeks, rental_replacement_value)

            disk.update_history(vehicle, rental_price, weeks, rental_replacement_value, total_cost)


            print('\n\nCalculating Your Total Price...\n\n')
            time.sleep(1.3)
            print('\n\n\nThank You! Your Total Price Is $' + str(total_cost))

        elif choice == '8':
            vehicle = '2015 Ford F-150 Platiunum King Ranch FX-4'
            vehicle_quantity = slow_type('\n\nHow Many ' + vehicle + ' Vehicles Would You Like To Rent From Us? ')
            weeks = slow_type('\n\nHow Many Weeks Would You Like To Rent This Vehicle? ')


            rental_price = disk.return_price(choice)

            rental_replacement_value = disk.return_replacement_value(choice)

            total_cost = core2.total_rental_cost(rental_price, weeks, rental_replacement_value)

            disk.update_history(vehicle, rental_price, weeks, rental_replacement_value, total_cost)


            print('\n\nCalculating Your Total Price...\n\n')
            time.sleep(1.3)
            print('\n\n\nThank You! Your Total Price Is $' + str(total_cost))

        elif choice == '9':
            vehicle = '2013 Ford F-150 Raptor'
            vehicle_quantity = slow_type('\n\nHow Many ' + vehicle + ' Vehicles Would You Like To Rent From Us? ')
            weeks = slow_type('\n\nHow Many Weeks Would You Like To Rent This Vehicle? ')


            rental_price = disk.return_price(choice)

            rental_replacement_value = disk.return_replacement_value(choice)

            total_cost = core2.total_rental_cost(rental_price, weeks, rental_replacement_value)

            disk.update_history(vehicle, rental_price, weeks, rental_replacement_value, total_cost)


            print('\n\nCalculating Your Total Price...\n\n')
            time.sleep(1.3)
            print('\n\n\nThank You! Your Total Price Is $' + str(total_cost))

        elif choice == '10':
            vehicle = '2017 Ford F-250 PowerStroke FX-4'
            vehicle_quantity = slow_type('\n\nHow Many ' + vehicle + ' Vehicles Would You Like To Rent From Us? ')
            weeks = slow_type('\n\nHow Many Weeks Would You Like To Rent This Vehicle? ')


            rental_price = disk.return_price(choice)

            rental_replacement_value = disk.return_replacement_value(choice)

            total_cost = core2.total_rental_cost(rental_price, weeks, rental_replacement_value)

            disk.update_history(vehicle, rental_price, weeks, rental_replacement_value, total_cost)


            print('\n\nCalculating Your Total Price...\n\n')
            time.sleep(1.3)
            print('\n\n\nThank You! Your Total Price Is $' + str(total_cost))

    elif option == '2':
        print('\n\nYou are returning a vehicle.... One moment while we load inventory...')
        time.sleep(3)


        disk.inventory()
        time.sleep(1)


        returning_vehicle = slow_type('\n\nWhat Vehicle Are You Returning Today? ')

        if returning_vehicle == '1':
            vehicle = '2014 Chevrolet Silverado 1500 z71'
            weeks = slow_type('\n\nHow Many Weeks Did You Have This Vehicle? ')

            rental_replacement_value = disk.return_replacement_value(returning_vehicle)
            disk.return_vehicle('RETURN', vehicle, weeks, rental_replacement_value)

        elif returning_vehicle == '2':
            vehicle = '2013 Chevrolet Colorado z71'
            weeks = slow_type('\n\nHow Many Weeks Did You Have This Vehicle? ')

            rental_replacement_value = disk.return_replacement_value(returning_vehicle)
            disk.return_vehicle('RETURN', vehicle, weeks, rental_replacement_value)
        
        elif returning_vehicle == '3':
            vehicle = '2015 Chevrolet Tahoe 1500 z71'
            weeks = slow_type('\n\nHow Many Weeks Did You Have This Vehicle? ')

            rental_replacement_value = disk.return_replacement_value(returning_vehicle)
            disk.return_vehicle('RETURN', vehicle, weeks, rental_replacement_value)

        elif returning_vehicle == '4':
            vehicle = '2007 Chevrolet Silverado DuraMax 2500 HD z71 Unique Edition'
            weeks = slow_type('\n\nHow Many Weeks Did You Have This Vehicle? ')

            rental_replacement_value = disk.return_replacement_value(returning_vehicle)
            disk.return_vehicle('RETURN', vehicle, weeks, rental_replacement_value)

        elif returning_vehicle == '5':
            vehicle = '2013 GMC Sierra 1500 z71'
            weeks = slow_type('\n\nHow Many Weeks Did You Have This Vehicle? ')

            rental_replacement_value = disk.return_replacement_value(returning_vehicle)
            disk.return_vehicle('RETURN', vehicle, weeks, rental_replacement_value)

        elif returning_vehicle == '6':
            vehicle = '2011 GMC Sierra 2500 DuraMax HD z71'
            weeks = slow_type('\n\nHow Many Weeks Did You Have This Vehicle? ')

            rental_replacement_value = disk.return_replacement_value(returning_vehicle)
            disk.return_vehicle('RETURN', vehicle, weeks, rental_replacement_value)

        elif returning_vehicle == '7':
            vehicle = '2017 GMC Yukon Denali High Country HD z71'
            weeks = slow_type('\n\nHow Many Weeks Did You Have This Vehicle? ')

            rental_replacement_value = disk.return_replacement_value(returning_vehicle)
            disk.return_vehicle('RETURN', vehicle, weeks, rental_replacement_value)

        elif returning_vehicle == '8':
            vehicle = '2015 Ford F-150 Platiunum King Ranch'
            weeks = slow_type('\n\nHow Many Weeks Did You Have This Vehicle? ')

            rental_replacement_value = disk.return_replacement_value(returning_vehicle)
            disk.return_vehicle('RETURN', vehicle, weeks, rental_replacement_value)

        elif returning_vehicle == '9':
            vehicle = '2013 Ford F-150 Raptor'
            weeks = slow_type('\n\nHow Many Weeks Did You Have This Vehicle? ')

            rental_replacement_value = disk.return_replacement_value(returning_vehicle)
            disk.return_vehicle('RETURN', vehicle, weeks, rental_replacement_value)

        elif returning_vehicle == '10':
            vehicle = '2017 Ford F-250 Powerstroke HD FX-4'
            weeks = slow_type('\n\nHow Many Weeks Did You Have This Vehicle? ')

            rental_replacement_value = disk.return_replacement_value(returning_vehicle)
            disk.return_vehicle('RETURN', vehicle, weeks, rental_replacement_value)

        time.sleep(1)
        print('\n\n Your Vehicle Has Been Successfully Returned. Thank You For Returning!')
        time.sleep(1)

    elif option == '3':
        print('\n\nLoading Transaction History...\n\n')
        time.sleep(1.5)
        disk.open_transaction_history_and_display()
        time.sleep(2)
        slow_type('\n\nPress "ENTER" To Go Back To Main!\n\n\n\n')
        main()

    time.sleep(1)
    print('\n\n\nGoodBye...')
    time.sleep(1)


if __name__ == '__main__':
    main()