import random
print("This is a Game of Stone, Paper and Scissor")
print("st for stone, s for scissor and p for paper")
l=["s","st","p"]
computerpoints=0
humanpoints=0
noofchoice=1
while noofchoice<11:
    human=input("Enter your choice for the game, you can enter 'st', 's' or 'p' only\n")
    computer=random.choice(l)
    if human=="st" and computer=="st":
        print("You both have chosen the same thing it's a draw and no point is given to anyone")
        humanpoints=humanpoints
        computerpoints=computerpoints
        print("Total no of choices you have remaining",10 - noofchoice,"choices")
    elif human=="s" and computer=="s":
        print("You both have chosen the same thing it's a draw and no point is given to anyone")
        humanpoints=humanpoints
        computerpoints=computerpoints
        print("The number of choices you have remaining", 10 - noofchoice,"choices")
    elif human=="p" and computer=="p":
        print("You both have chosen the same thing it's a draw and no point is given to anyone")
        humanpoints=humanpoints
        computerpoints=computerpoints
        print("The number of choices you haveremaining", 10 - noofchoice,"choices")
    elif human=="st" and computer=="s":
        print("Here human got win as stone can kill scissor")
        humanpoints=humanpoints+1
        print("The number of choices you have remaining", 10 - noofchoice,"choices")
    elif human=="st" and computer=="p":
        print("Here computer got win as paper can kill stone")
        computerpoints=computerpoints+1
        print("The number of choices you have remaining", 10 - noofchoice,"choices")
    elif human=="s" and computer=="st":
        print("Here computer got win as stone can kill scissor")
        computerpoints=computerpoints+1
        print("The number of choices you have remaining", 10 - noofchoice,"choices")
    elif human=="s" and computer=="p":
        print("Here human got win as scissor can tear paper")
        humanpoints=humanpoints+1
        print("The number of choices you have remaining", 10 - noofchoice,"choices")
    elif human=="p" and computer=="st":
        print("Here human got win as paper can kill stone")
        humanpoints=humanpoints+1
        print("The number of choices you have remaining", 10 - noofchoice,"choices")
    elif human=="p" and computer=="s":
        print("Here computer got win as scissor can tear paper")
        computerpoints=computerpoints+1
        print("The number of choices you have remaining", 10 - noofchoice,"choices")
    else:
        print("You have given the wrong input")
        break
    noofchoice=noofchoice+1

print("Your points are ",humanpoints)
print("Computer points are ",computerpoints)
if noofchoice==11:
    print("Game over")

print("\n The Result is announced\n")
if humanpoints>computerpoints:
    print("You got win")
elif humanpoints<computerpoints:
    print("Computer got win")
else:
    print("The points are equal it got tie")
