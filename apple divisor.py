try:
    apple = int(input("How many apples does Shubham have?\n"))
    minstud = int(input("What is the minimum range of student\t"))
    maxstud = int(input("What is the maximum range of student\t"))
except ValueError:
    print("Enter correct input")
    exit()

if minstud>maxstud:
    print("Enter correct number as minimum number cannot be greater than maximum number")

for i in range(minstud,maxstud+1):
    if apple%i==0:
        print(f"{i} is divisor of the number {apple}")
    elif apple%i>=1:
        print(f"{i} is not divisor of the number {apple}")
    elif minstud==maxstud:
        print("It is not range as it is equal")
