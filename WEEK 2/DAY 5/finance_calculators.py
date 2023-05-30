import re
import math

global_selection = ''

def selection():
    global global_selection
    global_selection = input("Please select either 'Investment' or 'Bond': ")

def investment():
    global global_selection  # Assuming `global_selection` is a global variable
    
    if re.match(r'(?i)investment', global_selection):
        type = input("Please select either 'Simple' or 'Compound': ")
        
        if re.match(r'(?i)simple', type):
            deposit = float(input("Enter the amount you would like to deposit: "))
            years = float(input("Enter the number of years that the money is being invested for: "))
            interest = float(input("Enter the interest rate: "))
            amount = deposit * (1 + (interest / 100) * years)
            print(str(amount))
            
        elif re.match(r'(?i)compound', type):
            deposit = float(input("Enter the amount you would like to deposit: "))
            years = float(input("Enter the number of years that the money is being invested for: "))
            interest = float(input("Enter the interest rate: "))
            amount = deposit * math.pow((1 + interest / 100), years)
            print(str(amount))
            
    elif re.match(r'(?i)bond', global_selection):
        present_value = float(input("Please enter the present value of the house: "))
        interest_rate = float(input("Please enter the interest rate: ")) / 12
        months = float(input("Enter the number of months over which the bond will be repaid: "))
        amount = (interest_rate/100 * present_value) / (1 - math.pow((1 + interest_rate/100), -months))
        print(str(amount))
print("Choose either 'investment' or 'bond' from the menu below to proceed:")
print("investment - to calculate the amount of interest you'll earn on interest")
print("bond - to calculate the amount you'll have to pay on a home loan")
selection()
investment()