import random
def chosen_game(a,b,actual):
    num = int(input(f"Enter the Number between {a} and {b}\n"))
    choice=1
    while num != actual:
        if num>=a and num<b:
            if num > actual:
                print("Your Entered number is greater than the Guessing Number, Enter again\n")
                num = int(input(f"Enter the Number between {a} and {b}\n"))
                choice=choice+1
            elif num < actual:
                print("Your Entered number is less than the Guessing Number,Enter again\n")
                num = int(input(f"Enter the Number between {a} and {b}\n"))
                choice=choice+1
            else:
                print("You Guessed correctly")
        else:
            print(f"You might have not entered the number between {a} and {b}")
    print(f"You guesses the number in {choice} guess.")
    return choice

a = int(input("Enter Number for Lower Bound Range\n"))
b = int(input("Enter Number for Upper Bound Range\n"))
actual1 = random.randint(a,b)
actual2 = random.randint(a,b)
print("Player1 turn\n")
g1 = chosen_game(a,b,actual1)
print("Player2 turn\n")
g2 = chosen_game(a,b,actual2)

if g1 > g2:
    print("Player2 won the game")
elif g1 < g2:
    print("Player1 won the game")
else:
    print("It's a tie")