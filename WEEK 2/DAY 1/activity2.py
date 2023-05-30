citi_burger = 22.00
citi_pie = 12.00
sausage_russianroll = 13.00
russianroll_and_chips = 20.00
small_chips = 10.00
big_chips = 20.00
coke = 9.00
order = 0
bill = 0.00

print(" 1.  CiTi burger             R22.00 \n 2.  CiTi pie                R12.00 \n 3.  Sausage/Russian roll    R13.00 \n 4.  Russian roll and chips  R20.00 \n 5. Small chips             R10.00 \n 6.  Big chips               R20.00 \n 7. Coke (350ml)            R9.00")

while order == 0: 
    order = float(input("What would you like to order?"))

    if order == 1:
        bill = citi_burger
        print("Total: R" + str(bill))
    
    if order == 2:
        bill = citi_pie
        print("Total: R" + str(bill))

    if order == 3:
        bill = sausage_russianroll
        print("Total: R" + str(bill))

    if order == 4:
        bill = russianroll_and_chips
        print("Total: R" + str(bill))
    
    if order == 5:
        bill = small_chips
        print("Total: R" + str(bill))

    if order == 6:
        bill = big_chips
        print("Total: R" + str(bill))

    if order == 7:
        bill = coke
        print("Total: R" + str(bill))

    elif order > 7 or order < 1:
        print("Sorry, you’ve entered an invalid number!")