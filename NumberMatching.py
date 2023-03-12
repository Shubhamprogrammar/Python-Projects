try:
    num1 = int(input("Enter the Number for Lower Bound range\n"))
    num2 = int(input("Enter the Number for Outer bound range\n"))
    if num1 > num2:
        print(f"The {num2} can't be greater than {num1}")
        exit()
except Exception as e:
    print("Enter numbers only")

import random
choose = random.randint(num1,num2)
noofchoice = 0
print("Player1:\n\nPlayer1 is playing the Game now!")
while True:
    try:
        num = int(input(f"Enter number to play the Game between the {num1} and {num2}\t"))
        if num>=num1 and num<=num2:
            if num==choose:
                print(f"You Guessed correctly in {noofchoice + 1} times")
                noofchoice=noofchoice+1
                break
            elif num > choose:
                print("Your Entered number is greater than the Guessing Number")
                noofchoice=noofchoice+1
            else:
                print("Your Entered number is less than the Guessing Number")
                noofchoice=noofchoice+1
        else:
            print(f"You might have not entered the number between {num1} and {num2}")
            noofchoice=1000000000
            break
    except Exception as e:
        print("You are getting one chance again play it properly")

choice = 0
print("Player2:\n\nNow it's the turn of Player2!")
choosen = random.randint(num1,num2)
while True:
    try:
        num = int(input(f"Enter number to play the Game between the {num1} and {num2}\t"))
        if num>=num1 and num<=num2:
            if num==choosen:
                print(f"You Guessed correctly in {choice +1} times")
                choice=choice+1
                break
            elif num > choosen:
                print("Your Entered number is greater than the Guessing Number")
                choice=choice+1
            else:
                print("Your Entered number is less than the Guessing Number")
                choice=choice+1
        else:
            print(f"You might have not entered the number between {num1} and {num2}")
            choice=10000000000000
            break
    except Exception as e:
        print("You are getting one chance again play it properly")

if choice > noofchoice:
    print(f"Player1 wins the game as He Guess the Number Correctly in less time and His Total Number of Guessing is {noofchoice}")
elif choice < noofchoice:
    print(f"Player2 wins the Game as He Guess the Number Correctly in less time and His Total Number of Guessing is {choice}")
else:
    print("No one wins the game as it is equal")