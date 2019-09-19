# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 19:04:26 2019
@author: Jonathan
"""
#Project 2
import math

print("\nWelcome to car rentals. \n")
print("At the prompts, please enter the following: ")
print("\tCustomer's classification code (a character: BDW) ")
print("\tNumber of days the vehicle was rented (int)")
print("\tOdometer reading at the start of the rental period (int)")
print("\tOdometer reading at the end of the rental period (int)")


while True:
#------------------------"Would you like to continue?" Prompts-----------------   
  first_input = input("\nWould you like to continue (Y/N)? ")
  if first_input == "Y" or first_input == "y": 
    classification = input("\nCustomer code (BDW): ")

    if classification == "B" or classification == "b": 
        days_rented = int(input("\nNumber of days: "))

        base_money_owed = days_rented * 40 #$40 a day

        starting_odometer = int(input("Odometer reading at the start: "))
        final_odometer = int(input("Odometer reading at the end:   "))
        if starting_odometer > final_odometer: #if the start odometer reading is larger than the final reading:
          adjustment1 = (999999 - starting_odometer) #Calculates out how close the initial odometer is to 000000.
          adjustment2 = (1 + adjustment1 + final_odometer) #calculates actual miles driven from a start number that's larger than the end.
          real_miles_driven = adjustment2 / 10 #ACTUAL CALCULATED mileage to be multiplied by mileage charge 
          mileage_cost = real_miles_driven * 0.25
          total_sum = float(mileage_cost + base_money_owed)
          rounded_sum = round(total_sum, 2)
          print("\nCustomer summary:")

          print("\tclassification code:", classification)

          print("\trental period (days): ", days_rented)

          print("\todometer reading at start:", starting_odometer)

          print("\todometer reading at end:  ", final_odometer)

          print("\tnumber of miles driven:", real_miles_driven)

          print("\tamount due: $",rounded_sum)

          continue #return to original statement
        elif starting_odometer < final_odometer:
          odometer_miles = final_odometer - starting_odometer
          real_miles_driven = odometer_miles / 10
          mileage_cost = real_miles_driven * 0.25
          total_sum = float(mileage_cost + base_money_owed)
          rounded_sum = round(total_sum, 2)
          print("\nCustomer summary:")

          print("\tclassification code:", classification)

          print("\trental period (days): ", days_rented)

          print("\todometer reading at start:", starting_odometer)

          print("\todometer reading at end:  ", final_odometer)

          print("\tnumber of miles driven:", real_miles_driven)

          print("\tamount due: $",rounded_sum)
          continue
      
    elif classification == "D" or classification == "d": 
        days_rented = int(input("\nNumber of days: "))
        base_money_owed = days_rented * 60 #$60 a day

        starting_odometer = int(input("Odometer reading at the start: "))
        final_odometer = int(input("Odometer reading at the end:   "))
        
        if starting_odometer > final_odometer: #if the start odometer reading is larger than the final reading:
          adjustment1 = (999999 - starting_odometer) #Calculates out how close the initial odometer is to 000000.
          adjustment2 = (1 + adjustment1 + final_odometer) #calculates actual miles driven from a start number that's larger than the end.
          real_miles_driven = adjustment2 / 10 #ACTUAL CALCULATED mileage to be multiplied by mileage charge
          average_miles_driven = real_miles_driven / days_rented
          adjusted_miles = average_miles_driven - 100

          if average_miles_driven <= 100:
            total_sum = float(base_money_owed) 
            rounded_sum = round(total_sum, 2)
            print("\nCustomer summary:")

            print("\tclassification code:", classification)

            print("\trental period (days): ", days_rented)

            print("\todometer reading at start:", starting_odometer)

            print("\todometer reading at end:  ", final_odometer)

            print("\tnumber of miles driven:", real_miles_driven)

            print("\tamount due: $",rounded_sum)
            continue #return to original statement

          elif average_miles_driven > 100:
            adjusted_miles = average_miles_driven - 100
            mileage_cost = (adjusted_miles * 0.25) + 60
            total_sum = float(mileage_cost * days_rented) 
            rounded_sum = round(total_sum, 2)   
            print("\nCustomer summary:")

            print("\tclassification code:", classification)

            print("\trental period (days): ", days_rented)

            print("\todometer reading at start:", starting_odometer)

            print("\todometer reading at end:  ", final_odometer)
 
            print("\tnumber of miles driven:", real_miles_driven)

            print("\tamount due: $",rounded_sum)        
            continue #return to original statement

        elif starting_odometer < final_odometer:
          odometer_miles = final_odometer - starting_odometer
          real_miles_driven = odometer_miles / 10
          average_miles_driven = real_miles_driven / days_rented
          if average_miles_driven <= 100:
            total_sum = float(base_money_owed)
            rounded_sum = round(total_sum, 2)
            print("\nCustomer summary:")

            print("\tclassification code:", classification)

            print("\trental period (days): ", days_rented)

            print("\todometer reading at start:", starting_odometer)

            print("\todometer reading at end:  ", final_odometer)

            print("\tnumber of miles driven:", real_miles_driven)

            print("\tamount due: $",rounded_sum)
            continue

          elif average_miles_driven > 100:
            adjusted_miles = average_miles_driven - 100
            mileage_cost = (adjusted_miles * 0.25) + 60
            total_sum = float(mileage_cost * days_rented) 
            rounded_sum = round(total_sum, 2)   
            print("\nCustomer summary:")

            print("\tclassification code:", classification)

            print("\trental period (days): ", days_rented)

            print("\todometer reading at start:", starting_odometer)

            print("\todometer reading at end:  ", final_odometer)

            print("\tnumber of miles driven:", real_miles_driven)

            print("\tamount due: $",rounded_sum)
            continue

    elif classification == "W" or classification == "w": 
        days_rented = int(input("\nNumber of days: "))
        weeks_rented = (days_rented / 7)
        ceil_weeks_rented = math.ceil(weeks_rented) #takes the ceiling 
        base_money_owed = ceil_weeks_rented * 190 #$190 / week

        starting_odometer = int(input("Odometer reading at the start: "))
        final_odometer = int(input("Odometer reading at the end:   "))
        
        if starting_odometer > final_odometer: #if the start odometer reading is larger than the final reading:
          adjustment1 = (999999 - starting_odometer) #Calculates out how close the initial odometer is to 000000.
          adjustment2 = (1 + adjustment1 + final_odometer) #calculates actual miles driven from a start number that's larger than the end.
          real_miles_driven = adjustment2 / 10 #ACTUAL CALCULATED mileage to be multiplied by mileage charge
          average_miles_per_week = real_miles_driven / ceil_weeks_rented

          if average_miles_per_week <= 900:
            total_sum = float(190 * ceil_weeks_rented)
            rounded_sum = round(total_sum, 2)
            print("\nCustomer summary:")

            print("\tclassification code:", classification)

            print("\trental period (days): ", days_rented)

            print("\todometer reading at start:", starting_odometer)

            print("\todometer reading at end:  ", final_odometer)

            print("\tnumber of miles driven:", real_miles_driven)

            print("\tamount due: $",rounded_sum)
            continue #return to original statement

          elif average_miles_per_week <= 1500:
            sum1 = (ceil_weeks_rented * 100)
            sum2 = ceil_weeks_rented * 190
            total_sum = float(sum1 + sum2)
            rounded_sum = round(total_sum, 2)
            print("\nCustomer summary:")

            print("\tclassification code:", classification)

            print("\trental period (days): ", days_rented)

            print("\todometer reading at start:", starting_odometer)

            print("\todometer reading at end:  ", final_odometer)

            print("\tnumber of miles driven:", real_miles_driven)

            print("\tamount due: $",rounded_sum)
            continue #return to original statement            
            
          else:
            adjusted_miles = average_miles_per_week - 1500 #(real_miles_driven / ceil_weeks_rented) - 1500
            sum1 = (200 * ceil_weeks_rented)
            special_sum = 62.5 * ceil_weeks_rented
            sum2 = (0.25 * adjusted_miles)
            total_sum = float(sum1 + sum2 + base_money_owed + special_sum)
            rounded_sum = round(total_sum, 2)     
            print("\nCustomer summary:")
            print("\tclassification code:", classification)
            print("\trental period (days): ", days_rented)
            print("\todometer reading at start:", starting_odometer)
            print("\todometer reading at end:  ", final_odometer)
            print("\tnumber of miles driven:", real_miles_driven)
            print("\tamount due: $",rounded_sum)
            continue #return to original statement
 


        elif starting_odometer < final_odometer:
          odometer_miles = final_odometer - starting_odometer
          real_miles_driven = odometer_miles / 10.0 #ACTUAL CALCULATED mileage to be multiplied by mileage charge     
          average_miles_per_week = real_miles_driven / ceil_weeks_rented

          if average_miles_per_week <= 900.0:
            total_sum = float(190.0 * ceil_weeks_rented)
            rounded_sum = round(total_sum, 2)
            print("\nCustomer summary:")
            print("\tclassification code:", classification)
            print("\trental period (days):", days_rented)
            print("\todometer reading at start:", starting_odometer)
            print("\todometer reading at end:  ", final_odometer)
            print("\tnumber of miles driven: ", real_miles_driven)
            print("\tamount due: $",rounded_sum)
            continue #return to original statement

          elif average_miles_per_week <=1500.0:
            sum1 = (ceil_weeks_rented * 100.0)
            sum2 = ceil_weeks_rented * 190.0
            total_sum = float(sum1 + sum2)
            rounded_sum = round(total_sum, 2)
            print("\nCustomer summary:")
            print("\tclassification code:", classification)
            print("\trental period (days):", days_rented)
            print("\todometer reading at start:", starting_odometer)
            print("\todometer reading at end:  ", final_odometer)
            print("\tnumber of miles driven: ", real_miles_driven)
            print("\tamount due: $",rounded_sum)
            continue #return to original statement            
            
          else:
              fixed_mile = average_miles_per_week - 1500 #(real_miles_driven / ceil_weeks_rented) - 1500
              charged_mile = (fixed_mile * ceil_weeks_rented) #fixed miles multiplied by amount of weeks
              price_charged_miles = charged_mile * 0.25
              sum1 = (200 * ceil_weeks_rented)
              sum2 = (190 * ceil_weeks_rented)
              total_sum = float(price_charged_miles + sum1 + sum2)
              rounded_sum = round(total_sum, 2)   
              print("\nCustomer summary:")
              print("\tclassification code:", classification)
              print("\trental period (days):", days_rented)
              print("\todometer reading at start:", starting_odometer)
              print("\todometer reading at end:  ", final_odometer)
              print("\tnumber of miles driven: ", real_miles_driven)
              print("\tamount due: $",rounded_sum)           
              continue #return to original statement
    else:
      print("\n\t*** Invalid customer code. Try again. ***")
      continue
    
  elif first_input == "N" or first_input == "n":
      print("Thank you for your loyalty.")
      break
  else:
      print("\n\t*** Invalid customer code. Try again. ***")
      continue
###########################################################################################################################