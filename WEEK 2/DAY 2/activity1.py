tempreature1 = float(input("Enter the temperature[in degrees Fahrenheit (° F) for day 1]: "))
tempreature2 = float(input("Enter the temperature[in degrees Fahrenheit (° F) for day 2]: "))
temp1_celsius = 0
temp2_celsius = 0

def Celsius():
    global temp1_celsius
    global temp2_celsius
    temp1_celsius = 5 / 9 * (tempreature1 - 32)
    temp2_celsius = 5 / 9 * (tempreature2 - 32)

def Conversion():
    print("Day 1 temperature in degrees Celsius (° C) is: " + str(temp1_celsius))
    print("Day 2 temperature in degrees Celsius (° C) is: " + str(temp2_celsius))
    if temp1_celsius > temp2_celsius: 
        print("Day 2 was the coldest")
    elif temp2_celsius > temp1_celsius:
        print("Day 1 was the coldest")
    else:
        print("The temperature was the same, thus it was equally as cold")

Celsius()
Conversion()