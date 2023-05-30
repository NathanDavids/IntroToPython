luxury = 0
commercial = 0
sedan = 0

cars = ["", "Luxury", "Commercial", "Sedan"]
car_input = 2
while car_input != 0:
    car_input = int(input("Please select a car? (1-3)"))

    if car_input == 0:
        print("Cars: " + "Luxury: " + str(luxury) + " " + "Commercial: " + str(commercial) + " " + "Sedan: " + str(sedan))

    if car_input == 1: 
        luxury += 1
        print("Cars: " + "Luxury: " + str(luxury) + " " +  "Commercial: " + str(commercial) + " " + "Sedan: " + str(sedan))

    if car_input == 2:
        commercial += 1
        print("Cars: " + "Luxury: " + str(luxury) + " " +"Commercial: " + str(commercial) + " " + "Sedan: " + str(sedan))

    if car_input == 3:
        sedan += 1
        print("Cars: " + "Luxury: " + str(luxury) + " " + "Commercial: " + str(commercial) + " " +"Sedan: " + str(sedan))