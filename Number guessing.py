winning_number=10
print("This is Number Guessing Game and it is limted to only 9 times")

num= int(input('Guess your Number between 1 to 100:-\n'))
guess = 1

while guess<=9:
    if (winning_number==num):
        print(f"You win! and you guess this number in {guess} time ")
        break
    elif (winning_number > num):
        print("Your guess is too low!")
        guess +=1
        num = int(input('Guess again\n'))
    else:
        print("Your guess is high")
        guess +=1
        num = int(input("Guess again\n"))
    print(9-guess,'No. of guesses left')
        
if guess>9:
        print('Game Over')
        

        