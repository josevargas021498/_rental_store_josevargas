import time, sys
import core
import disk




def main():

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
        vehicles = {'\n1. 2014 Chevrolet Silverado 2500 z71': 5, '\n2. 2013 Chervolet Colorado 4wd': 4, '\n3. 2015 Chevrolet Tahoe 1500 z71': 3, '\n4. 2007 Chevrolet Silverado DuraMax 2500 HD z71 Unique Edition': 1}
        for vehicle in vehicles.items():
            print (vehicle[0], vehicle[1])


    def silverado(details):
        """(str) -> (str)
        Prints details for Chevrolet Silverado 2500 z71.
        """
        details = [
            'Make And Model:', 'Chevrolet Silverado 2500 z71',
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
            '\nRental Cost *Per Week* :', '$300',
            '\nTOTAL RETAIL PRICE: ', '$41,800'

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
            '\n\n\nRental Cost *Per Week* : $200'
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
                    '\nRental Cost *Per Week* : ', '$385',
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
            '\nRent Cost *Per Week* : ', '$1,000',
            '\nTOTAL RETAIL PRICE: ', '$100,000'
        ]

        for detail in details:
            print(detail)

    def list_gmc_vehicles():
        """(str) -> (str)
        Prints vehicles for the brand GMC.
        """
        vehicles = [
            '\n1. 2013 GMC Sierra 1500 z71',
            '\n2. 2011 GMC Sierra 2500 HD DuraMax z71',
            '\n3. 2017 GMC Yukon Denali High Country HD z71'
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
            '\nRental Cost *Per Week* : ', '$340',
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
                    '\nRental Cost *Per Week* : ', '$500',
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
            '\nRental Cost *Per Week* : ', '$430',
            '\n\nTOTAL RETAIL PRICE: ' , '$53,700'
        ]
        for detail in details:
            print(detail)

    def list_ford_vehicles():
        """(str) -> (str)
        Prints Ford Brand Vehicles.
        """
        vehicles = [
            '\n1. 2015 Ford F-150 Platinum King Ranch',
            '\n2. 2013 Ford F-150 Raptor',
            '\n3. 2017 Ford F-250 PowerStroke\n'
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
            '\nRent Cost *Per Week* : ', '$350',
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
            '\nRent Cost *Per Week* :', '$550',
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
            '\nRent Cost *Per Week* : ', '$450',
            '\nTOTAL RETAIL PRICE: ', '$59,900\n'
        ]

        for detail in details: 
            print(detail)

    def check_out():
                        vehicle_rent = int(weeks) * step_2
                        sales_tax = 0.07
                        total_tax = int(vehicle_rent) * float(sales_tax) + int(vehicle_rent)
                        replacement_value = 0.10 * vehicle_retail_price
                        total_cost = total_tax + replacement_value
                        print('Thank You For Renting From Vargas\' Off-Road Rentals! \n\nYour Total Rent Cost is ' + '$' + str(total_cost) + '. Have A Wonderful Day!')

    def totaled():
        sales_tax = 0.07
        totaled_vehicle_price = replacement_value * sales_tax + replacement_value
        print('I Am Very Sorry About Your Accident. Your Replacement Cost is $' + str(replacement_value) + ' plus 7% tax, \n\nWhich Equals to $' + str(totaled_vehicle_price))
    
    def damaged():
        sales_tax = 0.07
        damaged_vehicle_cost = int(damage_cost) * sales_tax + int(damage_cost)
        print('\n\nI Am Very Sorry About Your Accident. Your Damage Cost Is', damage_cost, 'plus 7% tax, \n\nWhich Equals to $' + str(damaged_vehicle_cost))


    print('\n\nWELCOME TO VARGAS\' OFF-ROAD RENTALS!')
    time.sleep(1)

    slow_type('\n\n\n\nTo Look At Our List Of Options, Please Press "ENTER"\n\nRemember To Look At Our Inventory Before You Rent!(:\n\n')
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
                step_2 == 300
                vehicle_retail_price = 41800
                slow_type('\n\nPlease Hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n')
                silverado(details)
                time.sleep(1.5)
                slow_type('\n\nTo Proceed Please Press "ENTER".\n\n\n\n')
                    
                slow_type('\n\n\nYOU ARE ABOUT TO ENTER THE APPLICATION MODE.\n PLEASE ENTER ALL INFORMATION AS ACCURATE TO YOUR KNOWLEDGE AS POSSIBLE.\n \
                IF YOU ARE ASKED TO ENTER A WORD OR ANY ALPHABETIC CHARACTER,\n PLEASE DO SO WITH REASONABLE LENGHT. (SHORT) \n \
                IF YOU ARE ASKED TO ENTER A NUMBER, PLEASE DO SO ACCURATELY.\n ANY OF THE INFORMATION YOU ENTER MAY BE USED IN THE FUTURE.\n\n\nPRESS "ENTER"\n\n\n\n\n\n\n')
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading Application...\n')
                time.sleep(.8)
                print('\n\n                                                                       APPLICATION\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                time.sleep(1)
                name = slow_type('\n\nName: ')
                age = slow_type('\n\nAge: ')
                job = slow_type('\n\nJob: ')
                income = slow_type('\n\nWeekly Income: ')
                residency = slow_type('\n\nResidency *STATE ONLY* Ex:TX, NY, AL   : ')
                vehicle = slow_type('\nVehicle Renting: ')
                weeks = slow_type('\nWeeks Of Rent Desired -> *Notice We Our Least Period Of Time To Rent Is One Week* <- : ')
                
                time.sleep(.5)
                print('\n\n\n\n\n\n\n\nFinished Application...\n\n')
                time.sleep(1)
                slow_type('WE ARE ABOUT TO RUN YOUR APPLICATION THROUGH OUR SYSTEM.\n \
                RESULTS WILL BE PRESENTED AS "APPROVED" OR "DENIED".\n \
                IF YOUR ARE APPROVED, FURTHER INSTRUCTIONS WILL BE ASSIGNED.\n \
                IF YOU ARE DENIED, YOU WILL AUTOMATICALLY BE EJECTED FROM THIS PROGRAM.\n \
                \n\nTHANK YOU VERY MUCH FOR VISITING VARGAS\' OFF-ROAD RENTALS!!            Press "ENTER" ')
                time.sleep(2)
                print('\n\n\n\nProcessing Application...\n\n\n')
                time.sleep(1)
                print('\n\n\nWe Are Almost There...\n\n\n')
                time.sleep(2)
                slow_type('\n\nRESULTS RECEIVED!                PRESS "ENTER" TO VIEW. ')

                if age < '21':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, WE TRIED! BUT YOU MUST BE 21 OR OLDER TO RENT A VEHICLE FROM Us. \n\n\n                                   THANK YOU FOR CHOOSING US, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif income < '360':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! YOU MUST HAVE A WEEKLY INCOME OF AT LEAST $360 TO RENT THIS VEHICLE. \n\nTHANK YOU FOR CHOOSING VARGAS\' OFF-ROAD RENTALS, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif residency != 'MS':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, YOU MSUT BE A RESIDENT IN MISSISSIPPI.\n\n')
                    time.sleep(2)
                    exit()

                else:
                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n                                                               APPROVED!!\n\n\n\n\n\n\n\n\n\n\n')
                    time.sleep(2)

                    check_out()
                    print('\n\n\n\nLeaving Program...\n\n\n\n\n')
                    time.sleep(2)
                    
                        
                        
                
                
                


            elif step_2 == '2':
                step_2 == 200
                vehicle_retail_price = 26400
                slow_type('\n\nPlease Hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n\n')
                colorado_details(details)
                time.sleep(1.5)
                slow_type('\n\nTo Proceed Please Press "ENTER".\n\n\n\n')
                    
                slow_type('\n\n\nYOU ARE ABOUT TO ENTER THE APPLICATION MODE.\n PLEASE ENTER ALL INFORMATION AS ACCURATE TO YOUR KNOWLEDGE AS POSSIBLE.\n \
                IF YOU ARE ASKED TO ENTER A WORD OR ANY ALPHABETIC CHARACTER,\n PLEASE DO SO WITH REASONABLE LENGHT. (SHORT) \n \
                IF YOU ARE ASKED TO ENTER A NUMBER, PLEASE DO SO ACCURATELY.\n ANY OF THE INFORMATION YOU ENTER MAY BE USED IN THE FUTURE.\n\n\nPRESS "ENTER"\n\n\n\n\n\n\n')
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading Application...\n')
                time.sleep(.8)
                print('\n\n                                                                       APPLICATION\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                time.sleep(1)
                name = slow_type('\n\nName: ')
                age = slow_type('\n\nAge: ')
                job = slow_type('\n\nJob: ')
                income = slow_type('\n\nWeekly Income: ')
                residency = slow_type('\n\nResidency *STATE ONLY* Ex:TX, NY, AL   : ')
                vehicle = slow_type('\nVehicle Renting: ')
                weeks = slow_type('\nWeeks Of Rent Desired -> *Notice We Our Least Period Of Time To Rent Is One Week* <- : ')
                
                time.sleep(.5)
                print('\n\n\n\n\n\n\n\nFinished Application...\n\n')
                time.sleep(1)
                slow_type('WE ARE ABOUT TO RUN YOUR APPLICATION THROUGH OUR SYSTEM.\n \
                RESULTS WILL BE PRESENTED AS "APPROVED" OR "DENIED".\n \
                IF YOUR ARE APPROVED, FURTHER INSTRUCTIONS WILL BE ASSIGNED.\n \
                IF YOU ARE DENIED, YOU WILL AUTOMATICALLY BE EJECTED FROM THIS PROGRAM.\n \
                \n\nTHANK YOU VERY MUCH FOR VISITING VARGAS\' OFF-ROAD RENTALS!!            Press "ENTER" ')
                time.sleep(2)
                print('\n\n\n\nProcessing Application...\n\n\n')
                time.sleep(1)
                print('\n\n\nWe Are Almost There...\n\n\n')
                time.sleep(2)
                slow_type('\n\nRESULTS RECEIVED!                PRESS "ENTER" TO VIEW. ')

                if age < '21':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, WE TRIED! BUT YOU MUST BE 21 OR OLDER TO RENT A VEHICLE FROM Us. \n\n\n                                   THANK YOU FOR CHOOSING US, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif income < '300':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! YOU MUST HAVE A WEEKLY INCOME OF AT LEAST $300 TO RENT THIS VEHICLE. \n\nTHANK YOU FOR CHOOSING VARGAS\' OFF-ROAD RENTALS, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif residency != 'MS':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, YOU MSUT BE A RESIDENT IN MISSISSIPPI.\n\n')
                    time.sleep(2)
                    exit()

                else:
                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n                                                               APPROVED!!\n\n\n\n\n\n\n\n\n\n\n')
                    time.sleep(2)

                    check_out()
                    print('\n\n\n\nLeaving Program...\n\n\n\n\n')
                    time.sleep(2)
                    
                    
            elif step_2 == '3':
                step_2 = 385
                vehicle_retail_price = 54200
                slow_type('\n\nPlease Hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n\n')       
                tahoe(details)
                time.sleep(1.5)
                slow_type('\n\nTo Proceed Please Press "ENTER".\n\n\n\n')
                    
                slow_type('\n\n\nYOU ARE ABOUT TO ENTER THE APPLICATION MODE.\n PLEASE ENTER ALL INFORMATION AS ACCURATE TO YOUR KNOWLEDGE AS POSSIBLE.\n \
                IF YOU ARE ASKED TO ENTER A WORD OR ANY ALPHABETIC CHARACTER,\n PLEASE DO SO WITH REASONABLE LENGHT. (SHORT) \n \
                IF YOU ARE ASKED TO ENTER A NUMBER, PLEASE DO SO ACCURATELY.\n ANY OF THE INFORMATION YOU ENTER MAY BE USED IN THE FUTURE.\n\n\nPRESS "ENTER"\n\n\n\n\n\n\n')
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading Application...\n')
                time.sleep(.8)
                print('\n\n                                                                       APPLICATION\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                time.sleep(1)
                name = slow_type('\n\nName: ')
                age = slow_type('\n\nAge: ')
                job = slow_type('\n\nJob: ')
                income = slow_type('\n\nWeekly Income: ')
                residency = slow_type('\n\nResidency *STATE ONLY* Ex:TX, NY, AL   : ')
                vehicle = slow_type('\nVehicle Renting: ')
                weeks = slow_type('\nWeeks Of Rent Desired -> *Notice We Our Least Period Of Time To Rent Is One Week* <- : ')
                
                time.sleep(.5)
                print('\n\n\n\n\n\n\n\nFinished Application...\n\n')
                time.sleep(1)
                slow_type('WE ARE ABOUT TO RUN YOUR APPLICATION THROUGH OUR SYSTEM.\n \
                RESULTS WILL BE PRESENTED AS "APPROVED" OR "DENIED".\n \
                IF YOUR ARE APPROVED, FURTHER INSTRUCTIONS WILL BE ASSIGNED.\n \
                IF YOU ARE DENIED, YOU WILL AUTOMATICALLY BE EJECTED FROM THIS PROGRAM.\n \
                \n\nTHANK YOU VERY MUCH FOR VISITING VARGAS\' OFF-ROAD RENTALS!!            Press "ENTER" ')
                time.sleep(2)
                print('\n\n\n\nProcessing Application...\n\n\n')
                time.sleep(1)
                print('\n\n\nWe Are Almost There...\n\n\n')
                time.sleep(2)
                slow_type('\n\nRESULTS RECEIVED!                PRESS "ENTER" TO VIEW. ')

                if age < '21':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, WE TRIED! BUT YOU MUST BE 21 OR OLDER TO RENT A VEHICLE FROM Us. \n\n\n                                   THANK YOU FOR CHOOSING US, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif income < '400':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! YOU MUST HAVE A WEEKLY INCOME OF AT LEAST $460 TO RENT THIS VEHICLE. \n\nTHANK YOU FOR CHOOSING VARGAS\' OFF-ROAD RENTALS, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif residency != 'MS':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, YOU MSUT BE A RESIDENT IN MISSISSIPPI.\n\n')
                    time.sleep(2)
                    exit()

                else:
                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n                                                               APPROVED!!\n\n\n\n\n\n\n\n\n\n\n')
                    time.sleep(2)

                    check_out()
                    print('\n\n\n\nLeaving Program...\n\n\n\n\n')
                    time.sleep(2)
                    
            elif step_2 == '4':
                step_2 = 1000
                vehicle_retail_price = 100000 
                slow_type('\n\nPlease Hit "Enter" To See Details On This Vehicle...\n\n\n\n\n\n')
                silverado_duramax()
                time.sleep(1.5)
                slow_type('\n\nTo Proceed Please Press "ENTER".\n\n\n\n')
                    
                slow_type('\n\n\nYOU ARE ABOUT TO ENTER THE APPLICATION MODE.\n PLEASE ENTER ALL INFORMATION AS ACCURATE TO YOUR KNOWLEDGE AS POSSIBLE.\n \
                IF YOU ARE ASKED TO ENTER A WORD OR ANY ALPHABETIC CHARACTER,\n PLEASE DO SO WITH REASONABLE LENGHT. (SHORT) \n \
                IF YOU ARE ASKED TO ENTER A NUMBER, PLEASE DO SO ACCURATELY.\n ANY OF THE INFORMATION YOU ENTER MAY BE USED IN THE FUTURE.\n\n\nPRESS "ENTER"\n\n\n\n\n\n\n')
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading Application...\n')
                time.sleep(.8)
                print('\n\n                                                                       APPLICATION\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                time.sleep(1)
                name = slow_type('\n\nName: ')
                age = slow_type('\n\nAge: ')
                job = slow_type('\n\nJob: ')
                income = slow_type('\n\nWeekly Income: ')
                residency = slow_type('\n\nResidency *STATE ONLY* Ex:TX, NY, AL   : ')
                vehicle = slow_type('\nVehicle Renting: ')
                weeks = slow_type('\nWeeks Of Rent Desired -> *Notice We Our Least Period Of Time To Rent Is One Week* <- : ')
                
                time.sleep(.5)
                print('\n\n\n\n\n\n\n\nFinished Application...\n\n')
                time.sleep(1)
                slow_type('WE ARE ABOUT TO RUN YOUR APPLICATION THROUGH OUR SYSTEM.\n \
                RESULTS WILL BE PRESENTED AS "APPROVED" OR "DENIED".\n \
                IF YOUR ARE APPROVED, FURTHER INSTRUCTIONS WILL BE ASSIGNED.\n \
                IF YOU ARE DENIED, YOU WILL AUTOMATICALLY BE EJECTED FROM THIS PROGRAM.\n \
                \n\nTHANK YOU VERY MUCH FOR VISITING VARGAS\' OFF-ROAD RENTALS!!            Press "ENTER" ')
                time.sleep(2)
                print('\n\n\n\nProcessing Application...\n\n\n')
                time.sleep(1)
                print('\n\n\nWe Are Almost There...\n\n\n')
                time.sleep(2)
                slow_type('\n\nRESULTS RECEIVED!                PRESS "ENTER" TO VIEW. ')

                if age < '21':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, WE TRIED! BUT YOU MUST BE 21 OR OLDER TO RENT A VEHICLE FROM Us. \n\n\n                                   THANK YOU FOR CHOOSING US, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif income < '1200':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! YOU MUST HAVE A WEEKLY INCOME OF AT LEAST $1,200 TO RENT THIS VEHICLE. \n\nTHANK YOU FOR CHOOSING VARGAS\' OFF-ROAD RENTALS, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif residency != 'MS':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, YOU MSUT BE A RESIDENT IN MISSISSIPPI.\n\n')
                    time.sleep(2)
                    exit()

                else:
                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n                                                               APPROVED!!\n\n\n\n\n\n\n\n\n\n\n')
                    time.sleep(2)

                    check_out()
                    print('\n\n\n\nLeaving Program...\n\n\n\n\n')
                    time.sleep(2)     


        elif brand_choice == '2':
            slow_type('\n\nTo Look At The List Of Vehicles Of This Brand Press "ENTER".\n\n\n')
            list_gmc_vehicles()
            step_2 = slow_type('\n\nWhich Vehicle Suits You The Best? Please Choose.\n\n')
            if step_2 == '1':
                step_2 = 400
                vehicle_retail_price = 39800
                slow_type('\n\nPlease Hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n')
                sierra()
                time.sleep(1.5)
                slow_type('\n\nTo Proceed Please Press "ENTER".\n\n\n\n')
                    
                slow_type('\n\n\nYOU ARE ABOUT TO ENTER THE APPLICATION MODE.\n PLEASE ENTER ALL INFORMATION AS ACCURATE TO YOUR KNOWLEDGE AS POSSIBLE.\n \
                IF YOU ARE ASKED TO ENTER A WORD OR ANY ALPHABETIC CHARACTER,\n PLEASE DO SO WITH REASONABLE LENGHT. (SHORT) \n \
                IF YOU ARE ASKED TO ENTER A NUMBER, PLEASE DO SO ACCURATELY.\n ANY OF THE INFORMATION YOU ENTER MAY BE USED IN THE FUTURE.\n\n\nPRESS "ENTER"\n\n\n\n\n\n\n')
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading Application...\n')
                time.sleep(.8)
                print('\n\n                                                                       APPLICATION\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                time.sleep(1)
                name = slow_type('\n\nName: ')
                age = slow_type('\n\nAge: ')
                job = slow_type('\n\nJob: ')
                income = slow_type('\n\nWeekly Income: ')
                residency = slow_type('\n\nResidency *STATE ONLY* Ex:TX, NY, AL   : ')
                vehicle = slow_type('\nVehicle Renting: ')
                weeks = slow_type('\nWeeks Of Rent Desired -> *Notice We Our Least Period Of Time To Rent Is One Week* <- : ')
                
                time.sleep(.5)
                print('\n\n\n\n\n\n\n\nFinished Application...\n\n')
                time.sleep(1)
                slow_type('WE ARE ABOUT TO RUN YOUR APPLICATION THROUGH OUR SYSTEM.\n \
                RESULTS WILL BE PRESENTED AS "APPROVED" OR "DENIED".\n \
                IF YOUR ARE APPROVED, FURTHER INSTRUCTIONS WILL BE ASSIGNED.\n \
                IF YOU ARE DENIED, YOU WILL AUTOMATICALLY BE EJECTED FROM THIS PROGRAM.\n \
                \n\nTHANK YOU VERY MUCH FOR VISITING VARGAS\' OFF-ROAD RENTALS!!            Press "ENTER" ')
                time.sleep(2)
                print('\n\n\n\nProcessing Application...\n\n\n')
                time.sleep(1)
                print('\n\n\nWe Are Almost There...\n\n\n')
                time.sleep(2)
                slow_type('\n\nRESULTS RECEIVED!                PRESS "ENTER" TO VIEW. ')

                if age < '21':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, WE TRIED! BUT YOU MUST BE 21 OR OLDER TO RENT A VEHICLE FROM Us. \n\n\n                                   THANK YOU FOR CHOOSING US, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif income < '400':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! YOU MUST HAVE A WEEKLY INCOME OF AT LEAST $400 TO RENT THIS VEHICLE. \n\nTHANK YOU FOR CHOOSING VARGAS\' OFF-ROAD RENTALS, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif residency != 'MS':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, YOU MSUT BE A RESIDENT IN MISSISSIPPI.\n\n')
                    time.sleep(2)
                    exit()

                else:
                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n                                                               APPROVED!!\n\n\n\n\n\n\n\n\n\n\n')
                    time.sleep(2)

                    check_out()
                    print('\n\n\n\nLeaving Program...\n\n\n\n\n')
                    time.sleep(2)
                    
                    

            elif step_2 == '2':
                step_2 = 500
                vehicle_retail_price = 57500
                slow_type('\n\nPlease hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n')
                sierra_duramax()
                time.sleep(1.5)
                slow_type('\n\nTo Proceed Please Press "ENTER".\n\n\n\n')
                    
                slow_type('\n\n\nYOU ARE ABOUT TO ENTER THE APPLICATION MODE.\n PLEASE ENTER ALL INFORMATION AS ACCURATE TO YOUR KNOWLEDGE AS POSSIBLE.\n \
                IF YOU ARE ASKED TO ENTER A WORD OR ANY ALPHABETIC CHARACTER,\n PLEASE DO SO WITH REASONABLE LENGHT. (SHORT) \n \
                IF YOU ARE ASKED TO ENTER A NUMBER, PLEASE DO SO ACCURATELY.\n ANY OF THE INFORMATION YOU ENTER MAY BE USED IN THE FUTURE.\n\n\nPRESS "ENTER"\n\n\n\n\n\n\n')
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading Application...\n')
                time.sleep(.8)
                print('\n\n                                                                       APPLICATION\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                time.sleep(1)
                name = slow_type('\n\nName: ')
                age = slow_type('\n\nAge: ')
                job = slow_type('\n\nJob: ')
                income = slow_type('\n\nWeekly Income: ')
                residency = slow_type('\n\nResidency *STATE ONLY* Ex:TX, NY, AL   : ')
                vehicle = slow_type('\nVehicle Renting: ')
                weeks = slow_type('\nWeeks Of Rent Desired -> *Notice We Our Least Period Of Time To Rent Is One Week* <- : ')
                
                time.sleep(.5)
                print('\n\n\n\n\n\n\n\nFinished Application...\n\n')
                time.sleep(1)
                slow_type('WE ARE ABOUT TO RUN YOUR APPLICATION THROUGH OUR SYSTEM.\n \
                RESULTS WILL BE PRESENTED AS "APPROVED" OR "DENIED".\n \
                IF YOUR ARE APPROVED, FURTHER INSTRUCTIONS WILL BE ASSIGNED.\n \
                IF YOU ARE DENIED, YOU WILL AUTOMATICALLY BE EJECTED FROM THIS PROGRAM.\n \
                \n\nTHANK YOU VERY MUCH FOR VISITING VARGAS\' OFF-ROAD RENTALS!!            Press "ENTER" ')
                time.sleep(2)
                print('\n\n\n\nProcessing Application...\n\n\n')
                time.sleep(1)
                print('\n\n\nWe Are Almost There...\n\n\n')
                time.sleep(2)
                slow_type('\n\nRESULTS RECEIVED!                PRESS "ENTER" TO VIEW. ')

                if age < '21':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, WE TRIED! BUT YOU MUST BE 21 OR OLDER TO RENT A VEHICLE FROM Us. \n\n\n                                   THANK YOU FOR CHOOSING US, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif income < '580':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! YOU MUST HAVE A WEEKLY INCOME OF AT LEAST $580 TO RENT THIS VEHICLE. \n\nTHANK YOU FOR CHOOSING VARGAS\' OFF-ROAD RENTALS, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif residency != 'MS':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, YOU MSUT BE A RESIDENT IN MISSISSIPPI.\n\n')
                    time.sleep(2)
                    exit()

                else:
                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n                                                               APPROVED!!\n\n\n\n\n\n\n\n\n\n\n')
                    time.sleep(2)

                    check_out()
                    print('\n\n\n\nLeaving Program...\n\n\n\n\n')
                    time.sleep(2)
                    
                    
            elif step_2 == '3':
                step_2 = 430
                vehicle_retail_price = 53700
                slow_type('\n\nPlease hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n')
                denali()
                time.sleep(1.5)
                slow_type('\n\nTo Proceed Please Press "ENTER".\n\n\n\n')
                    
                slow_type('\n\n\nYOU ARE ABOUT TO ENTER THE APPLICATION MODE.\n PLEASE ENTER ALL INFORMATION AS ACCURATE TO YOUR KNOWLEDGE AS POSSIBLE.\n \
                IF YOU ARE ASKED TO ENTER A WORD OR ANY ALPHABETIC CHARACTER,\n PLEASE DO SO WITH REASONABLE LENGHT. (SHORT) \n \
                IF YOU ARE ASKED TO ENTER A NUMBER, PLEASE DO SO ACCURATELY.\n ANY OF THE INFORMATION YOU ENTER MAY BE USED IN THE FUTURE.\n\n\nPRESS "ENTER"\n\n\n\n\n\n\n')
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading Application...\n')
                time.sleep(.8)
                print('\n\n                                                                       APPLICATION\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                time.sleep(1)
                name = slow_type('\n\nName: ')
                age = slow_type('\n\nAge: ')
                job = slow_type('\n\nJob: ')
                income = slow_type('\n\nWeekly Income: ')
                residency = slow_type('\n\nResidency *STATE ONLY* Ex:TX, NY, AL   : ')
                vehicle = slow_type('\nVehicle Renting: ')
                weeks = slow_type('\nWeeks Of Rent Desired -> *Notice We Our Least Period Of Time To Rent Is One Week* <- : ')
                
                time.sleep(.5)
                print('\n\n\n\n\n\n\n\nFinished Application...\n\n')
                time.sleep(1)
                slow_type('WE ARE ABOUT TO RUN YOUR APPLICATION THROUGH OUR SYSTEM.\n \
                RESULTS WILL BE PRESENTED AS "APPROVED" OR "DENIED".\n \
                IF YOUR ARE APPROVED, FURTHER INSTRUCTIONS WILL BE ASSIGNED.\n \
                IF YOU ARE DENIED, YOU WILL AUTOMATICALLY BE EJECTED FROM THIS PROGRAM.\n \
                \n\nTHANK YOU VERY MUCH FOR VISITING VARGAS\' OFF-ROAD RENTALS!!            Press "ENTER" ')
                time.sleep(2)
                print('\n\n\n\nProcessing Application...\n\n\n')
                time.sleep(1)
                print('\n\n\nWe Are Almost There...\n\n\n')
                time.sleep(2)
                slow_type('\n\nRESULTS RECEIVED!                PRESS "ENTER" TO VIEW. ')

                if age < '21':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, WE TRIED! BUT YOU MUST BE 21 OR OLDER TO RENT A VEHICLE FROM Us. \n\n\n                                   THANK YOU FOR CHOOSING US, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif income < '500':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! YOU MUST HAVE A WEEKLY INCOME OF AT LEAST $500 TO RENT THIS VEHICLE. \n\nTHANK YOU FOR CHOOSING VARGAS\' OFF-ROAD RENTALS, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif residency != 'MS':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, YOU MSUT BE A RESIDENT IN MISSISSIPPI.\n\n')
                    time.sleep(2)
                    exit()

                else:
                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n                                                               APPROVED!!\n\n\n\n\n\n\n\n\n\n\n')
                    time.sleep(2)

                    check_out()
                    print('\n\n\n\nLeaving Program...\n\n\n\n\n')
                    time.sleep(2)
                    
                    
        elif brand_choice == '3':
            slow_type('\n\nTo Look At The List Of Vehicles Of This Brand Press "ENTER".\n\n\n')
            list_ford_vehicles()
            time.sleep(1.5)

            step_2 = slow_type('\n\nWhich Vehicle Suits You The Best? Please Choose.\n\n')
            if step_2 == '1':
                step_2 = 350
                vehicle_retail_price = 44800
                slow_type('\n\n\nPlease Hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n')
                f150_platinum()
                time.sleep(1.5)
                slow_type('\n\nTo Proceed Please Press "ENTER".\n\n\n\n')
                    
                slow_type('\n\n\nYOU ARE ABOUT TO ENTER THE APPLICATION MODE.\n PLEASE ENTER ALL INFORMATION AS ACCURATE TO YOUR KNOWLEDGE AS POSSIBLE.\n \
                IF YOU ARE ASKED TO ENTER A WORD OR ANY ALPHABETIC CHARACTER,\n PLEASE DO SO WITH REASONABLE LENGHT. (SHORT) \n \
                IF YOU ARE ASKED TO ENTER A NUMBER, PLEASE DO SO ACCURATELY.\n ANY OF THE INFORMATION YOU ENTER MAY BE USED IN THE FUTURE.\n\n\nPRESS "ENTER"\n\n\n\n\n\n\n')
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading Application...\n')
                time.sleep(.8)
                print('\n\n                                                                       APPLICATION\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                time.sleep(1)
                name = slow_type('\n\nName: ')
                age = slow_type('\n\nAge: ')
                job = slow_type('\n\nJob: ')
                income = slow_type('\n\nWeekly Income: ')
                residency = slow_type('\n\nResidency *STATE ONLY* Ex:TX, NY, AL   : ')
                vehicle = slow_type('\nVehicle Renting: ')
                weeks = slow_type('\nWeeks Of Rent Desired -> *Notice We Our Least Period Of Time To Rent Is One Week* <- : ')
                
                time.sleep(.5)
                print('\n\n\n\n\n\n\n\nFinished Application...\n\n')
                time.sleep(1)
                slow_type('WE ARE ABOUT TO RUN YOUR APPLICATION THROUGH OUR SYSTEM.\n \
                RESULTS WILL BE PRESENTED AS "APPROVED" OR "DENIED".\n \
                IF YOUR ARE APPROVED, FURTHER INSTRUCTIONS WILL BE ASSIGNED.\n \
                IF YOU ARE DENIED, YOU WILL AUTOMATICALLY BE EJECTED FROM THIS PROGRAM.\n \
                \n\nTHANK YOU VERY MUCH FOR VISITING VARGAS\' OFF-ROAD RENTALS!!            Press "ENTER" ')
                time.sleep(2)
                print('\n\n\n\nProcessing Application...\n\n\n')
                time.sleep(1)
                print('\n\n\nWe Are Almost There...\n\n\n')
                time.sleep(2)
                slow_type('\n\nRESULTS RECEIVED!                PRESS "ENTER" TO VIEW. ')

                if age < '21':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, WE TRIED! BUT YOU MUST BE 21 OR OLDER TO RENT A VEHICLE FROM Us. \n\n\n                                   THANK YOU FOR CHOOSING US, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif income < '400':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! YOU MUST HAVE A WEEKLY INCOME OF AT LEAST $400 TO RENT THIS VEHICLE. \n\nTHANK YOU FOR CHOOSING VARGAS\' OFF-ROAD RENTALS, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif residency != 'MS':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, YOU MSUT BE A RESIDENT IN MISSISSIPPI.\n\n')
                    time.sleep(2)
                    exit()

                else:
                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n                                                               APPROVED!!\n\n\n\n\n\n\n\n\n\n\n')
                    time.sleep(2)

                    check_out()
                    print('\n\n\n\nLeaving Program...\n\n\n\n\n')
                    time.sleep(2)
                    
                    
            elif step_2 == '2':
                step_2 = 550
                vehicle_retail_price = 68900
                slow_type('\n\n\nPlease Hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n')
                raptor()
                time.sleep(1.5)
                slow_type('\n\nTo Proceed Please Press "ENTER".\n\n\n\n')
                    
                slow_type('\n\n\nYOU ARE ABOUT TO ENTER THE APPLICATION MODE.\n PLEASE ENTER ALL INFORMATION AS ACCURATE TO YOUR KNOWLEDGE AS POSSIBLE.\n \
                IF YOU ARE ASKED TO ENTER A WORD OR ANY ALPHABETIC CHARACTER,\n PLEASE DO SO WITH REASONABLE LENGHT. (SHORT) \n \
                IF YOU ARE ASKED TO ENTER A NUMBER, PLEASE DO SO ACCURATELY.\n ANY OF THE INFORMATION YOU ENTER MAY BE USED IN THE FUTURE.\n\n\nPRESS "ENTER"\n\n\n\n\n\n\n')
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading Application...\n')
                time.sleep(.8)
                print('\n\n                                                                       APPLICATION\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                time.sleep(1)
                name = slow_type('\n\nName: ')
                age = slow_type('\n\nAge: ')
                job = slow_type('\n\nJob: ')
                income = slow_type('\n\nWeekly Income: ')
                residency = slow_type('\n\nResidency *STATE ONLY* Ex:TX, NY, AL   : ')
                vehicle = slow_type('\nVehicle Renting: ')
                weeks = slow_type('\nWeeks Of Rent Desired -> *Notice We Our Least Period Of Time To Rent Is One Week* <- : ')
                
                time.sleep(.5)
                print('\n\n\n\n\n\n\n\nFinished Application...\n\n')
                time.sleep(1)
                slow_type('WE ARE ABOUT TO RUN YOUR APPLICATION THROUGH OUR SYSTEM.\n \
                RESULTS WILL BE PRESENTED AS "APPROVED" OR "DENIED".\n \
                IF YOUR ARE APPROVED, FURTHER INSTRUCTIONS WILL BE ASSIGNED.\n \
                IF YOU ARE DENIED, YOU WILL AUTOMATICALLY BE EJECTED FROM THIS PROGRAM.\n \
                \n\nTHANK YOU VERY MUCH FOR VISITING VARGAS\' OFF-ROAD RENTALS!!            Press "ENTER" ')
                time.sleep(2)
                print('\n\n\n\nProcessing Application...\n\n\n')
                time.sleep(1)
                print('\n\n\nWe Are Almost There...\n\n\n')
                time.sleep(2)
                slow_type('\n\nRESULTS RECEIVED!                PRESS "ENTER" TO VIEW. ')

                if age < '21':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, WE TRIED! BUT YOU MUST BE 21 OR OLDER TO RENT A VEHICLE FROM Us. \n\n\n                                   THANK YOU FOR CHOOSING US, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif income < '700':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! YOU MUST HAVE A WEEKLY INCOME OF AT LEAST $700 TO RENT THIS VEHICLE. \n\nTHANK YOU FOR CHOOSING VARGAS\' OFF-ROAD RENTALS, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif residency != 'MS':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, YOU MSUT BE A RESIDENT IN MISSISSIPPI.\n\n')
                    time.sleep(2)
                    exit()

                else:
                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n                                                               APPROVED!!\n\n\n\n\n\n\n\n\n\n\n')
                    time.sleep(2)

                    check_out()
                    print('\n\n\n\nLeaving Program...\n\n\n\n\n')
                    time.sleep(2)
                    
                    
            elif step_2 == '3':
                step_2 = 450
                vehicle_retail_price = 59900
                slow_type('\n\n\nPlease Hit "ENTER" To See Details On This Vehicle...\n\n\n\n\n')
                powerstroke()
                time.sleep(1.5)
                slow_type('\n\nTo Proceed Please Press "ENTER".\n\n\n\n')
                    
                slow_type('\n\n\nYOU ARE ABOUT TO ENTER THE APPLICATION MODE.\n PLEASE ENTER ALL INFORMATION AS ACCURATE TO YOUR KNOWLEDGE AS POSSIBLE.\n \
                IF YOU ARE ASKED TO ENTER A WORD OR ANY ALPHABETIC CHARACTER,\n PLEASE DO SO WITH REASONABLE LENGHT. (SHORT) \n \
                IF YOU ARE ASKED TO ENTER A NUMBER, PLEASE DO SO ACCURATELY.\n ANY OF THE INFORMATION YOU ENTER MAY BE USED IN THE FUTURE.\n\n\nPRESS "ENTER"\n\n\n\n\n\n\n')
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading Application...\n')
                time.sleep(.8)
                print('\n\n                                                                       APPLICATION\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                time.sleep(1)
                name = slow_type('\n\nName: ')
                age = slow_type('\n\nAge: ')
                job = slow_type('\n\nJob: ')
                income = slow_type('\n\nWeekly Income: ')
                residency = slow_type('\n\nResidency *STATE ONLY* Ex:TX, NY, AL   : ')
                vehicle = slow_type('\nVehicle Renting: ')
                weeks = slow_type('\nWeeks Of Rent Desired -> *Notice We Our Least Period Of Time To Rent Is One Week* <- : ')
                
                time.sleep(.5)
                print('\n\n\n\n\n\n\n\nFinished Application...\n\n')
                time.sleep(1)
                slow_type('WE ARE ABOUT TO RUN YOUR APPLICATION THROUGH OUR SYSTEM.\n \
                RESULTS WILL BE PRESENTED AS "APPROVED" OR "DENIED".\n \
                IF YOUR ARE APPROVED, FURTHER INSTRUCTIONS WILL BE ASSIGNED.\n \
                IF YOU ARE DENIED, YOU WILL AUTOMATICALLY BE EJECTED FROM THIS PROGRAM.\n \
                \n\nTHANK YOU VERY MUCH FOR VISITING VARGAS\' OFF-ROAD RENTALS!!            Press "ENTER" ')
                time.sleep(2)
                print('\n\n\n\nProcessing Application...\n\n\n')
                time.sleep(1)
                print('\n\n\nWe Are Almost There...\n\n\n')
                time.sleep(2)
                slow_type('\n\nRESULTS RECEIVED!                PRESS "ENTER" TO VIEW. ')

                if age < '21':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, WE TRIED! BUT YOU MUST BE 21 OR OLDER TO RENT A VEHICLE FROM Us. \n\n\n                                   THANK YOU FOR CHOOSING US, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif income < '600':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! YOU MUST HAVE A WEEKLY INCOME OF AT LEAST $600 TO RENT THIS VEHICLE. \n\nTHANK YOU FOR CHOOSING VARGAS\' OFF-ROAD RENTALS, HAVE A GREAT DAY!')
                    time.sleep(2)
                    exit()
                elif residency != 'MS':
                    print('\n\nChallenging A Red Flag...\n\n')
                    time.sleep(1)
                    print('\n\n\n\n\n\n\n                                                                       DECLINED!  \n\n\n\n\n! SORRY, YOU MSUT BE A RESIDENT IN MISSISSIPPI.\n\n')
                    time.sleep(2)
                    exit()

                else:
                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n                                                               APPROVED!!\n\n\n\n\n\n\n\n\n\n\n')
                    time.sleep(2)

                    check_out()
                    print('\n\n\n\nLeaving Program...\n\n\n\n\n')
                    time.sleep(2)
                    
                    
            
            


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
                    print('\n\nLoading 2014 Chevrolet Silverado 2500 z71 Details...\n\n\n')
                    time.sleep(1)
                    silverado(details)
                    time.sleep(2)
                    EXIT= slow_type('To Check Another Vehicle Out Please Press "ENTER".            To EXIT Program Please Type "STOP". ')
                    if EXIT== 'STOP':
                        break
                    main()
                elif details == '2':
                    print('\n\nLoading 2013 Chevrolet Colorado z71 Details...\n\n')
                    time.sleep(2)
                    colorado_details(details)
                    time.sleep(2)
                    EXIT= slow_type('To Check Another Vehicle Out Please Press "ENTER".            To EXIT Program Please Type "STOP". ')
                    if EXIT== 'STOP':
                        break
                    main()
                elif details == '3':
                    print('\n\nLoading 2015 Chevrolet Tahoe 1500 z71 Details...\n\n')
                    time.sleep(2)
                    tahoe(details)
                    time.sleep(2)
                    EXIT= slow_type('To Check Another Vehicle Out Please Press "ENTER".            To EXIT Program Please Type "STOP". ')
                    if EXIT== 'STOP':
                        break
                    main()
                elif details == '4':
                    print('\n\nLoading 2007 Chevrolet Silverado DuraMax 2500 HD z71 Unique Edition Details...\n\n')
                    time.sleep(2)
                    silverado_duramax()
                    time.sleep(2)
                    EXIT= slow_type('To Check Another Vehicle Out Please Press "ENTER".            To EXIT Program Please Type "STOP". ')
                    if EXIT== 'STOP':
                        break
                    main()
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
                    EXIT= slow_type('To Check Another Vehicle Out Please Press "ENTER".            To EXIT Program Please Type "STOP". ')
                    if EXIT== 'STOP':
                        break
                    main()
                elif details == '2':
                    print('\n\n\nLoading 2011 GMC Sierra 2500 HD DuraMax z71 Details...\n\n\n\n')
                    time.sleep(2)
                    sierra_duramax()
                    time.sleep(2)
                    EXIT= slow_type('To Check Another Vehicle Out Please Press "ENTER".            To EXIT Program Please Type "STOP". ')
                    if EXIT== 'STOP':
                        break
                    main()
                elif details == '3':
                    print('\n\n\nLoading 2017 GMC Yukon Denali High Country HD z71 Details...\n\n\n')
                    time.sleep(2)
                    denali()
                    time.sleep(2)
                    EXIT= slow_type('To Check Another Vehicle Out Please Press "ENTER".            To EXIT Program Please Type "STOP". ')
                    if EXIT== 'STOP':
                        break
                    main()
            elif brand_choice == '3':
                print('\n\n\n\n\nLoading Ford Inventory...\n\n\n\n\n\n')
                time.sleep(2)
                list_ford_vehicles()
                time.sleep(2)
                details = slow_type('\n\n\nPlease Type The Option Number Of The Vehicle You Would Like To See Details On: ')

                if details == '1':
                    print('\n\n\nLoading  2015 Ford F-150 Platinum King Ranch Details...\n\n\n')
                    time.sleep(2)
                    f150_platinum()
                    time.sleep(2)
                    EXIT= slow_type('To Check Another Vehicle Out Please Press "ENTER".            To EXIT Program Please Type "STOP". ')
                    if EXIT== 'STOP':
                        break
                    main()
                elif details == '2':
                    print('\n\nLoading 2013 Ford F-150 Raptor Details...\n\n')
                    time.sleep(2)
                    raptor()
                    time.sleep(2)
                    EXIT= slow_type('To Check Another Vehicle Out Please Press "ENTER".            To EXIT Program Please Type "STOP". ')
                    if EXIT== 'STOP':
                        break
                    main()
                elif details == '3':
                    print('\n\nLoading 2017 Ford F-250 PowerStroke Details...\n\n')
                    time.sleep(2)
                    powerstroke()
                    time.sleep(2)
                    EXIT= slow_type('To Check Another Vehicle Out Please Press "ENTER".            To EXIT Program Please Type "STOP". ')
                    if EXIT== 'STOP':
                        break
                    main()


    elif step_1 == '4':
        print('\n\n\n\n\n\n\n\n\n\n\nLoading All Vehicles... \n\n')
        time.sleep(2)
        slow_type('All Vehicles Loaded! Press "ENTER"\n\n\n\n\n\n\n')
        list_vehicles()
        list_gmc_vehicles()
        list_ford_vehicles()
        time.sleep(1)
        slow_type('\n\nTo Go Back To Main Press "ENTER"...\n\n')
        print('Loading Main...')
        time.sleep(1)
        main()
    
    elif step_1 == '5':
        print('\n\nYou Are Repoting An Accident!\n\n')
        time.sleep(1.3)
        slow_type('\n\nPlease Fill In The Following Paperwork About Your Accident... \n\n\nPRESS "ENTER"\n\n\n')
        print_brands()
        brand_involved = slow_type('\n\nEnter Brand Of Vehicle Involved: ')
        if brand_involved == '1':
            list_vehicles()
            vehicle_involved = slow_type('\n\nEnter Vehicle Involved: ')
            
            if vehicle_involved == '1':
                type_of_accident = slow_type('\n\nWas This Vehicle "totaled" or "damaged"? : ')
                if type_of_accident == 'totaled':
                    replacement_value = 41800
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)

                    totaled()
                elif type_of_accident == 'damaged':
                    damage_cost = slow_type('\n\nHow Much Is The Damage Cost? : ')
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)
                    
                    damaged()


            
            elif vehicle_involved == '2':
                type_of_accident = slow_type('\n\nWas This Vehicle "totaled" or "damaged"? : ')
                if type_of_accident == 'totaled':
                    replacement_value = 26400
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)

                    totaled()
                elif type_of_accident == 'damaged':
                    damage_cost = slow_type('\n\nHow Much Is The Damage Cost? : ')
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)
                    
                    damaged()


            elif vehicle_involved == '3':
                type_of_accident = slow_type('\n\nWas This Vehicle "totaled" or "damaged"? : ')
                if type_of_accident == 'totaled':
                    replacement_value = 54200
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)

                    totaled()
                elif type_of_accident == 'damaged':
                    damage_cost = slow_type('\n\nHow Much Is The Damage Cost? : ')
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)
                    
                    damaged()


            elif vehicle_involved == '4':
                type_of_accident = slow_type('\n\nWas This Vehicle "totaled" or "damaged"? : ')
                if type_of_accident == 'totaled':
                    replacement_value = 100000
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)

                    totaled()

                elif type_of_accident == 'damaged':
                    damage_cost = slow_type('\n\nHow Much Is The Damage Cost? : ')
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)
                    
                    damaged()

        elif brand_involved == '2':
            list_gmc_vehicles()
            vehicle_involved = slow_type('\n\nEnter Vehicle Involved: ')
            
            if vehicle_involved == '1':
                type_of_accident = slow_type('\n\nWas This Vehicle "totaled" or "damaged"? : ')
                if type_of_accident == 'totaled':
                    replacement_value = 39800
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)

                    totaled()
                elif type_of_accident == 'damaged':
                    damage_cost = slow_type('\n\nHow Much Is The Damage Cost? : ')
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)
                    
                    damaged()

            
            elif vehicle_involved == '2':
                type_of_accident = slow_type('\n\nWas This Vehicle "totaled" or "damaged"? : ')
                if type_of_accident == 'totaled':
                    replacement_value = 57500
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)

                    totaled()
                elif type_of_accident == 'damaged':
                    damage_cost = slow_type('\n\nHow Much Is The Damage Cost? : ')
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)
                    
                    damaged()


            elif vehicle_involved == '3':
                type_of_accident = slow_type('\n\nWas This Vehicle "totaled" or "damaged"? : ')
                if type_of_accident == 'totaled':
                    replacement_value = 53700
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)

                    totaled()
                elif type_of_accident == 'damaged':
                    damage_cost = slow_type('\n\nHow Much Is The Damage Cost? : ')
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)
                    
                    damaged()


        elif brand_involved == '3':
            list_ford_vehicles()
            vehicle_involved = slow_type('\n\nEnter Vehicle Involved: ')
            
            if vehicle_involved == '1':
                type_of_accident = slow_type('\n\nWas This Vehicle "totaled" or "damaged"? : ')
                if type_of_accident == 'totaled':
                    replacement_value = 44800
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)

                    totaled()
                elif type_of_accident == 'damaged':
                    damage_cost = slow_type('\n\nHow Much Is The Damage Cost? : ')
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)
                    
                    damaged()
            
            elif vehicle_involved == '2':
                type_of_accident = slow_type('\n\nWas This Vehicle "totaled" or "damaged"? : ')
                if type_of_accident == 'totaled':
                    replacement_value = 68900
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)

                    totaled()
                elif type_of_accident == 'damaged':
                    damage_cost = slow_type('\n\nHow Much Is The Damage Cost? : ')
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)
                    
                    damaged()

            elif vehicle_involved == '3':
                type_of_accident = slow_type('\n\nWas This Vehicle "totaled" or "damaged"? : ')
                if type_of_accident == 'totaled':
                    replacement_value = 59900
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)

                    totaled()
                elif type_of_accident == 'damaged':
                    damage_cost = slow_type('\n\nHow Much Is The Damage Cost? : ')
                    print('\n\nCalculating...\n\n\n')
                    time.sleep(2)
                    
                    damaged()



if __name__ == '__main__':
    main()