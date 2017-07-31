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
    options_1 = [
        '\n1. Rent A Vehicle',
        '\n2. Return A Vehicle',
        '\n3. Look At Inventory',
        '\n4. Look At Completely Inventory',
        '\n5. Report An Accident'
    ]

    for option in options_1:
        print(option)

def print_brands():
    brands = [
        '1. Chevrolet',
        '2. GMC',
        '3. Ford'
    ]
    for brand in brands:
        print(brand)

def list_vehicles():
    vehicles = {'1. 2014 Chevrolet Silverado 2500 z71': 5, '2. 2013 Chervolet Colorado 4wd': 4, '3. 2015 Chevrolet Tahoe 1500 z71': 3, '4. 2007 Chevrolet Silverado DuraMax 2500 HD z71 Unique Edition': 1}
    for vehicle in vehicles.items():
        print (vehicle[0], vehicle[1])


def silverado(details):
    """(str) -> (str)
    Prints details for Chevrolet Silverado 2500 z71.
    """
    details = [
        '\nMake And Model:', 'Chevrolet Silverado 2500 z71',
        '\nYear Model:', '2013',
        '\nEngine:', '6.0L Vortec Max',
        '\nDrive Train:', '4WD',
        '\nFuel:', 'Gasoline',
        '\nColor:', 'Black',
        '\nCabin:', 'Crew Cab',
        '\nInterior:', 'Black Leather, Touch Screen Navigation Radio, Heated Seats, 5% Limo Tint All Around, Reverse Cameras',
        '\nExterior Off-Road Upgrades:', 'Yes',
        '\nLift:', '4.5 in. Suspension By Rough Country',
        '\nWheels:', '22 in. Monster XD',
        '\nTires:', 'Nitto Mud-Grappler',
        '\nLightening:', '52 in. Creed Light-Bar "24 in. In Front Brush-Guard, Halo Projector w/ 12000k Blue HID "Low&High"',
        '\nRe-Enforcement:', 'Ranch-Hand Brushguard ""Black" "Front&Back"',
        '\nTOTAL RETAIL PRICE: ', '$41,800\n'

    ]
    for detail in details:
        print(detail)




def colorado_details(details):
    """ (str) -> (str)
    Prints details for Chevrolet Colorado 4wd.
    """
    details = [
        '\n\n\nMake And Model: Chevrolet Silverado'
        '\n\n\nYear Model: 2012'
        '\n\n\nEngine: 3.5 L Vortec'
        '\n\n\nFuel: Gasoline'
        '\n\n\nDrive Train: 4WD'
        '\n\n\nColor: Silver'
        '\n\n\nCabin: Crew Cab'
        '\n\n\nInterior: Cloth, Touch Screen Navigating Radio, Roll Cage, 5% Limo Tint All Around'
        '\n\n\nExterior Off-Road Upgrades: Yes'
        '\n\n\nLift: 5 in. Suspension by Rough Country'
        '\n\n\nWheels: 22 in. Fuel Rims "BLACK"'
        '\n\n\nTires: 33 in. Nitto Trail-Grapplers'
        '\n\n\nLightening: 45 in. Creed Lightbar "24 in. In Front Bull-Bar", 10000K HId "Low&High" w/ Spider Halo Rings'
        '\n\n\nRe-Enforcement: Roll-Cage, Rough_Country Bull-Bar, Headlight & Tail-Light Covers'
        '\n\n\nTOTAL RETAIl PRICE:  $26,400\n'
    ]

    for detail in details:
        print(detail)

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

def silverado_duramax():
    """(str) -> (str)
    Prints Details For 2007 Chevrolet Silverado DuraMax 2500 HD z71 Unique Edition.
    """
    details = [
        '\nMake And Make Model: ', 'Chevrolet Silverado Duramax 2500 HD z71 *Unique Edition*',
        '\nYear Model: ', '2007',
        '\nEngine: ', '6.6 L Twin Turbo Supercharged DuraMax',
        '\nFuel: ', 'Diesel',
        '\nDrive Train: ', '4WD',
        '\nColor: ', 'Jet-Black',
        '\nCabin: ', 'Crew Cab', 
        '\nInterior: ', '0% Ultra Black Limo Tint All Around, Marines Radio, Fully Loaded Touch Screen Navigating Radio, Black-Out Mossy Oak Interionr, Camra Control w/ Lightening, Manual Operating System "Exterior Cameras and System Performance", Interior Lightbar Remote Controlling Via Touch Screen Panel, 15 in. Monitors for every Passanger, 8 in. Monitor in Steeriing Wheel, Surround Dobly Speakers "All Around You", A.C w/ Thermostat Control, Interior Blue Dim Lightning, Commant Prompt, Programmer Controller, Pressure, Meter, Temperature, and Charger Gauges, Windshield Reflection Speedometer And Cameras, Built-In Roll Cage, Sound Retriever "everything outside can be heard", Sun Roof "w/ Rack", Massagers In Seats',
        '\nExterior Off-Road Upgrades: ', 'Yes',
        '\nLift: ', '4.5 in. Rough Country Specialized',
        '\nWheels: ', '33 in. Rockstar XD 811 "Satin Black"',
        '\nTires: ', 'Nitto Mud Grapplers "Extreme Edition"',
        '\nLightening: ', 'BLACKED OUT EVERYTHING, Halo Spider Projector Headlights w/ 12000K HID "Low&High""Blacked Out", Police Interceptor Spot Lights "Driver&Pass.", "White Underglow", Full Front LED Lightening "Inside Grill and Bumpers", 4 in. Halo Pods On Fog Lights, Roof Rack w/ 52 in. Lightbar Around X4 "Creed", Go-Light, Rear 24 in. Creed Lightbar X2 "Tool Box", SpotLights by Remote Control In Fenders, LED Reverse Spider tailights',
        '\nRe-Enforcement: ', 'Full Marine Steel Grill + Bumper + Headlight  Guards + Hood + Fender, Metal Body, Full Marine Rear Bumper + Tail Gate + Tailight Guard, Windshield Protector Bar Cage, Lightbar Rack "Protector", HD Mirror Bar, Tire Armor',
        '\nTOTAL RETAIL PRICE: ', '$100,000'
    ]

    for detail in details:
        print(detail)

def list_gmc_vehicles():
    """(str) -> (str)
    Prints vehicles for the brand GMC.
    """
    vehicles = [
        '1. 2013 GMC Sierra 1500 z71',
        '2. 2011 GMC Sierra 2500 HD DuraMax z71',
        '3. 2017 GMC Yukon Denali High Country HD z71'
        ]
    
    for vehicle in vehicles:
        print(vehicle)

def sierra():
    """(str) -> (str)
    Prints Details For 2013 GMC Sierra 1500 z71
    """
    details = [
        '\nMake And Model: ', 'GMC Sierra 1500 z71',
        '\nYear Model: ', '2013',
        '\nEngine: ', '5.3 L Vortec',
        '\nFuel: ', 'Gasoline',
        '\nDrive Train: ', '4WD',
        '\nColor: ', 'Gray',
        '\nCabin: ', 'Crew Cab',
        '\nInterior: ', 'Touch Screen Navigation Radion, Monitor + TV Behind Pass.& Driver Seat, Surround Lightening, Black Leather, 5% Limo Tint (All Around), Heated seats',
        '\nExterior Off-Road Upgrades: ', 'Yes',
        '\nLift: ', '5 in. Suspension By Rough Country',
        '\nWheels: ', '20 in. Stock 2015 Rims ("Black&Chrome")',
        '\nTires: ', '33 in. Nitto Mud Grapplers',
        '\nLightening: ', 'K.C Fog Lights X2(Roof), 32 in. LED Light Bars X2(Reverse), Go Light',
        '\nRe-Enforcement: ', 'Ranch Hand Front Bumper "Black" w/ Grill Guard, Custom Rear Bumper Open Country "Black", Bush Wacker Fender Flares',
        '\nTOTAL RETAIL PRICE: ', '$39,800'
        ]
    for detail in details:
        print(detail)

def sierra_duramax():
                """(str)->(str)
                Prints Details For 2011 GMC Sierra 2500 HD DuraMax z71.
                """

                details = [
                    '\nMake And Make Model: ', 'GMC 2500 HD DuraMax z71',
                    '\nYear Model: ', '2011',
                    '\nEngine: ' , '6.6 L DuraMax V8 SuperCharged',
                    '\nFuel: ', 'Diesel',
                    '\nDrive Train: ', '4WD',
                    '\nColor: ', 'Brown',
                    '\nCabin: ', 'Crew Cab',
                    '\nInterior: ', 'Fully Loaded, HD Monitors All Around, Pressure Gauges, A.C (All Around), Black Leather Seats (Heated), 2.5% Limo Tint All Around, Allison Transmission Easy Manual Shifter, Bully Dog Programer',
                    '\nExterior Off-Road Upgrades: ', 'Yes',
                    '\nLift: ', '7.5 in. Suspension ("By Rough Country"), 2.5 in. Body ("By Rough Country")',
                    '\nWheels: ', '37 in. Moto Metal XtReMe Rims (Black)',
                    '\nTires: ', '40 in. low.prof Nitto Mud Grappler',
                    '\nLightening: ', '52 in. Halo Concepts Lightbar, 52 in. Creed Lightbar (STACKED IN ROOF RACK), Fog Life LED Spot Lights, 10000K Hid (low&high), 52 in. 6000K HID Projector (Reverse) By Rough Country)',
                    '\nRe-Enforcement: ', 'Full Rough Country Bumper Re-Enforcement (bumper"black", grill"black", brush guard "black"), Rear Bumper by Rough Country',
                    '\nTOTAL RETAIL PRICE: ', '$57,500'
                ]

                for detail in details:
                    print(detail)

def denali():
    """(str) -> (str)
    Prints Details For 2017 GMC Yukon Denali High Country HD z71.
    """
    details = [
        '\nMake And Model: ', 'GMC Yukon Denali High Country HD z71.',
        '\nYear Model: ', '2017',
        '\nEngine: ' '6.2 L Vortec L94',
        '\nFuel: ', 'Gasoline',
        '\nDrive Train: ', '4WD', 
        '\nColor: ', 'Silver Platinum',
        '\nCabin: ', 'Crew Cab',
        '\nInterior: ', 'Fully Loaded, Mossy Oak Interionr, Touch Screen Navigating Radio, Rear and Front Cameras, Heated Seats, Luxury Dash, 5% Limo Tint "All Around", Drink Holders "Keeps Them Cold", Roof Overview Camera, Satelite Overview screen + DVD Behind Front Two Seats',
        '\nExterior Off-Road Upgrades: ', 'Yes', 
        '\nLift: ', '6 in. Suspension By Rough Country', 
        '\nWheels: ', '22 in. WORX Platinum Rims "Black & Silver Platiunum',
        '\nTires: ', 'Nitto Trail Grappler',
        '\nLightening: ', 'Halo Concepts Projector On Headlights, Custom 12000K HID "Low&High", 52 in. Halo Concepts Lightbar "Hood", 32 in. Halo Concepts Lightbar "Brushguard", 12 in. Halo Concepts Lightbar X2 "Bed Rails""BACKWARDS", GO-Light',
        '\nRe-Enforcement: ', 'Custom Made Full Metal Fenders And Bumper + Grill, Costom Made Full Metal "Rear" Bumper, Bush-Waker Fender Flares, Windshield Pretection Bar,'
        '\n\nTOTAL RETAIL PRICE: ' , '$53,700'
    ]
    for detail in details:
        print(detail)

def list_ford_vehicles():
    """(str) -> (str)
    Prints Ford Brand Vehicles.
    """
    vehicles = [
        '1. 2015 Ford F-150 Platinum King Ranch',
        '2. 2013 Ford F-150 Raptor',
        '3. 2017 Ford F-250 PowerStroke'
    ]
    for vehicle in vehicles:
        print(vehicle)

def f150_platinum():
    """(str) -> (str)
    Prints Details For 2015 Ford F-150 King Ranch.
    """
    details = [
        '\nMake And Make Model: ', 'Ford F150 Platinum Kng Ranch',
        '\nYear Model: ', '2015', 
        '\nEngine: ', '5.4 L F15',
        '\nFuel: ', 'Gasoline',
        '\nDrive Train: ', '4WD',
        '\nColor: ', 'Characoal',
        '\nCabin: ', 'Crew Cap',
        '\nInterior: ', 'Touch Screen Navigating Radio, Fully Loaded, A.C, DVD Behind Front Seats',
        '\nExterior Off-Road Upgrades: ', 'Yes',
        '\nLift: ', '7.5 in. Suspension By Rough Country',
        '\nWheels: ', '35 in. Rockstar XD "BLACK"',
        '\nTires: ', '37 in. Nitto Mud Grapples',
        '\nLightening: ', '52 in. LED Lightbar "roof" ',
        '\nRe-Enforcement: ', 'Full Ranch Hand Bumper "Grille and Bumper + Headlight Protector + Windshield Bar Protector, Rear Full Ranch Hand Metal Guard "Tailights',
        '\nTOTAL RETAIL PRICE: ', '$44,800\n'
    ]
    
    for detail in details:
        print(detail)

def raptor():
    """(str) -> (str)
    Prints Details For 2013 Ford F-150 Raptor.
    """
    details = [
        '\nMake And Make Model: ', 'Ford F-150 Raptor',
        '\nYear Model: ', '2013',
        '\nEngine: ', '6.2 L Raptor',
        '\nFuel: ', 'Gasoline',
        '\nDrive Train: ', '4WD',
        '\nColor: ', 'Brown',
        '\nCabin: ', 'Crew Cab',
        '\nInterior: ', 'Touch Screen Navigation Radio, Exhaust Flow Control, Litter Control, Performance Control, Built In Programer, Black Leather, Flat Screen Plasma Dispay Behind Every Seat, XpLoDe Advanced Sound System, Manual Shifter Built-In',
        '\nExterior Off-Road Upgrades: ', 'Yes',
        '\nLift: ', 'Stock 3.5 in. Suspension By Raptor Team',
        '\nWheels: ', 'Special Edition 20 in. Stock By Ford',
        '\nTires: ', 'Nitto Mud Grapplers',
        '\nLightening: ', '52 in. Creed Lightbar "ROOF", Halo Concepts "HEADLIGHTS&TAILIGHTS", Go-Light, K.C Lights In BrushGuard, Reverse LED Pods',
        '\nRe-Enforcement: ', 'Ranch Hand Brush Guard, Bush Wacker Fender Flares, Roll Cage',
        '\nTOTAL RETAIL PRICE: ', '$68,900\n'
    ]
    for detail in details:
        print(detail)

def powerstroke():
    """(str) -> (str)
    Prints Details For 2017 Ford F-250 PowerStroke.
    """
    details = [
        '\nMake And Make Model: ', 'Ford F-250 PowerStroke',
        '\nYear Model: ', '2017',
        '\nEngine: ', '7.3 L PowerStroke',
        '\nFuel: ', 'Diesel',
        '\nDrive Train: ', '4WD',
        '\nColor: ', 'Black',
        '\nCabin: ', 'Crew Cab',
        '\nInterior: ', 'Touch Screen Navigating Radio, Touch Screen Air Control, Sensor Display In Plasma Screen, Custom Interior "Texas Leather", Rear A.C, Programer Control, Fully Loaded',
        '\nExterior Off-Road Upgrades: ', 'Yes',
        '\nLift: ', '4.5 in. Suspesion By Rough Country',
        '\nWheels: ', '35 in. Monster XD "Black&Silver" Rims',
        '\nTires: ', '40 in. Nitto Mud Grappler',
        '\nLightening: ', '52 in. Halo Concept Lightbar X2 "STACKED" "FRONTWARDS AND BACKWARDS", Blacked Out Halo Concept Headlights, Blacked Out Halo Taillights, 10000K HID "Low&High"',
        '\nRe-Enforcement: ', 'Ranch Hand Blacked Out Bumper, Ranch Hand Blacked Out Steel Rear Bumper, Rack Protector, Bush Wacker Fender Flares, Police Interceptor SpotLight "Driver Side"',
        '\nTOTAL RETAIL PRICE: ', '$59,900\n'
    ]

    for detail in details: 
        print(detail)

print('\n\nWELCOME TO VARGAS\' VEHICLE RENTAL COMPANY FOR OFFROAD!')
time.sleep(1)

slow_type('\n\n\n\nTo Look At Our List Of Options, Please Press "ENTER"\n\n')
print_options_1()
time.sleep(1)

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

        if step_2 == '1':
            slow_type('\n\nPlease Hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n')
            silverado(details)

        elif step_2 == '2':
            slow_type('\n\nPlease Hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n\n')
            colorado_details(details)
        
        elif step_2 == '3':
            slow_type('\n\nPlease Hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n\n')       
            tahoe(details)

        elif step_2 == '4':
            slow_type('\n\nPlease Hit "Enter" To See Details On This Vehicle...\n\n\n\n\n\n')
            silverado_duramax()



    elif brand_choice == '2':
        slow_type('\n\nTo Look At The List Of Vehicles Of This Brand Press "ENTER".\n\n\n')
        list_gmc_vehicles()
        step_2 = slow_type('\n\nWhich Vehicle Suits You The Best? Please Choose.\n\n')
        if step_2 == '1':
            slow_type('\n\nPlease Hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n')
            sierra()

        elif step_2 == '2':
            slow_type('\n\nPlease hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n')
            sierra_duramax()

        elif step_2 == '3':
             slow_type('\n\nPlease hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n')
             denali()

    elif brand_choice == '3':
        slow_type('\n\nTo Look At The List Of Vehicles Of This Brand Press "ENTER".\n\n\n')
        list_ford_vehicles()

        step_2 = slow_type('\n\nWhich Vehicle Suits You The Best? Please Choose.\n\n')
        if step_2 == '1':
            slow_type('\n\n\nPlease Hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n')
            f150_platinum()

        elif step_2 == '2':
            slow_type('\n\n\nPlease Hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n')
            raptor()

        elif step_2 == '3':
            slow_type('\n\n\nPlease Hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n')
            powerstroke()
            
        
        
            

# elif step_1 == '2':
#     #your code here


elif step_1 == '3':
    print('\n\n\n\nLoading...')
    time.sleep(1.1)
    slow_type('\n\nPlease Press Enter To View Our Inventory.')

    while True:
        print('\n\n\nLoading Brands...\n\n\n\n')
        time.sleep(1)
        print_brands()

        brand_choice = slow_type('\n\nWhich Brand Would You Like To View? \n\nEnter Option Number As Provided:  ')
        if brand_choice == '1':
            print('\n\n\n\n\n\n\n\nLoading Chevrolet Inventory...\n\n')
            time.sleep(2)
            list_vehicles()
            time.sleep(1)
            details = slow_type('\n\nPlease Enter The Option Number Of The Vehicle You Would Like to See Details On:  ')

            if details == '1':
                print('\n\nLoading 2014 Chevrolet Silverado 2500 z71...\n\n\n')
                time.sleep(1)
                silverado(details)
                time.sleep(2)
                exit = slow_type('To Check Another Vehicle Out Please Press "ENTER".            To Exit Program Please Type "STOP".')
                if exit == 'STOP':
                    break
            elif details == '2':
                print('\n\nLoading 2013 Chevrolet Colorado z71...\n\n')
                time.sleep(2)
                colorado_details(details)
                time.sleep(2)
                exit = slow_type('To Check Another Vehicle Out Please Press "ENTER".            To Exit Program Please Type "STOP".')
                if exit == 'STOP':
                    break
            elif details == '3':
                print('\n\nLoading 2015 Chevrolet Tahoe 1500 z71...\n\n')
                time.sleep(2)
                tahoe(details)
                time.sleep(2)
                exit = slow_type('To Check Another Vehicle Out Please Press "ENTER".            To Exit Program Please Type "STOP".')
                if exit == 'STOP':
                    break
            elif details == '4':
                print('\n\nLoading 2007 Chevrolet Silverado DuraMax 2500 HD z71 Unique Edition...\n\n')
                time.sleep(2)
                silverado_duramax()
                time.sleep(2)
                exit = slow_type('To Check Another Vehicle Out Please Press "ENTER".            To Exit Program Please Type "STOP".')
                if exit == 'STOP':
                    break
        elif brand_choice == '2':
            print('\n\n\n\n\n\nLoading GMC Inventory...\n\n\n\n\n')
            time.sleep(2)
            list_gmc_vehicles()
            time.sleep(2)
            details = slow_type('\n\nPlease Type The Option Number Of The Vehicle You Would Like To See Details On: ')
                
            if details == '1':
                print('\n\n\n\nLoading 2013 GMC Sierra 1500 z71 Details...\n\n\n\n')
                time.sleep(2)
                sierra()
                time.sleep(2)
                exit = slow_type('To Check Another Vehicle Out Please Press "ENTER".            To Exit Program Please Type "STOP".')
                if exit == 'STOP':
                    break
            elif details == '2':
                print('\n\n\nLoading 2011 GMC Sierra 2500 HD DuraMax z71 Details...\n\n\n\n')
                time.sleep(2)
                sierra_duramax()
                time.sleep(2)
                exit = slow_type('To Check Another Vehicle Out Please Press "ENTER".            To Exit Program Please Type "STOP".')
                if exit == 'STOP':
                    break
            elif details == '3':
                print('\n\n\nLoading 2017 GMC Yukon Denali High Country HD z71 Details...\n\n\n')
                time.sleep(2)
                denali()
                time.sleep(2)
                exit = slow_type('To Check Another Vehicle Out Please Press "ENTER".            To Exit Program Please Type "STOP".')
                if exit == 'STOP':
                    break
        elif brand_choice == '3':
            print('\n\n\n\n\nLoading Ford Inventory...\n\n\n\n\n\n')
            time.sleep(2)
            list_ford_vehicles()
            time.sleep(2)
            detials = slow_type('\n\n\nPlease Type The Option Number Of The Vehicle You Would Like To See Details On: ')

            if details == '1':
                print('\n\n\nLoading  2015 Ford F-150 Platinum King Ranch Details...\n\n\n')
                time.sleep(2)
                f150_platinum()
                time.sleep(2)
                exit = slow_type('To Check Another Vehicle Out Please Press "ENTER".            To Exit Program Please Type "STOP".')
                if exit == 'STOP':
                    break
            elif details == '2':
                print('\n\nLoading 2013 Ford F-150 Raptor Details...\n\n')
                time.sleep(2)
                raptor()
                time.sleep(2)
                exit = slow_type('To Check Another Vehicle Out Please Press "ENTER".            To Exit Program Please Type "STOP".')
                if exit == 'STOP':
                    break
            elif details == '3':
                print('\n\nLoading 2017 Ford F-250 PowerStroke Details...\n\n')
                time.sleep(2)
                powerstroke()
                time.sleep(2)
                exit = slow_type('To Check Another Vehicle Out Please Press "ENTER".            To Exit Program Please Type "STOP".')
                if exit == 'STOP':
                    break


# elif step_1 == '4':
#     #your code here

# elif step_1 == '5':
#     #your code here


# else:
#     your code here