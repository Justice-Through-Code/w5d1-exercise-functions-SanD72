# tip_calculator.py

# TODO: Create a function named calculate_tip
   # try:  #DO NOT MODIFY
def tip_calculator():

    # TODO:
        # Get these user inputs
        
        # total_cost (float): The cost of the meal (without tax)
    total_cost = float(input('The cost of the meal (without tax)'))
        # num_people (int): The number of people splitting the bill
    
    num_people = int(input('The number of people splitting the bill'))
        # tip_percentage (float): The tip percentage
    tip_percentage = float(input('What tip percentage would you like to leave? For example %20.: %  '))
        # calculate tip amount
    total_tip = total_cost * (tip_percentage /100) 

    
    # TODO:
        # Calculate the total bill including tip and sales tax (10%).
            # Convert to float: The total bill (including tip and sales tax).
            #I take total_cost and multiply it by 0.1 to get the amount of tax.
    total_bill = (total_cost * 0.1) + total_tip + total_cost
    # NOTE: Calculate the tip and tax separately. 
    #return total_bill
    # TODO: 
        # Calculate how much each person should pay.
        # Convert to float: The amount each person should pay.   
    split_check = total_bill / num_people
   
    # TODO:
        # Using an f-string, print two different statements 
        # Total bill: $0.00
        # Each person should pay: $0.00

    print(f'Total bill: ${total_bill:.2f}')
    print(f'Each person should pay: ${split_check:.2f}')
#except ValueError as ERROR:
#print('Input is invalid: {ERROR}')
#tip_calculator()

    # NOTE: The amounts are displayed with 2 decimals only
    # except: # TODO: modify this except to include a Built-in Exception
        # TODO: Print an statement telling the user their input is invalid  
    
if __name__ == "__main__": # DO NOT MODIFY
    tip_calculator() # DO NOT MODIFY

