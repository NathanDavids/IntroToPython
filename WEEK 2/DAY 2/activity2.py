import random

random_number = random.randint(0,20)
while True: 
    user_number = int(input("I am busy thinking of a number, can you guess it...? \n Guess the number between 1 and 20: "))
    if user_number > random_number:
        print("\n")
        print("Too High")
        print("\n")
    elif user_number < random_number:
        print("\n")
        print("Too Low")
        print("\n")
    else: 
        if user_number == random_number:
            print("\n")
            print("Congratulations, you've guessed it!")
            print("\n")
            break
         

