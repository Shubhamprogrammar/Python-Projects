l=[]
def log():
    b=input("What do you want to log, if you want to log for Study Enter 'study' or 's', if you want to log for Exercise Enter 'exercise' or 'e', if you want to log for food Enter 'food' or 'f'\n")
    if b=="study" or b=="s":
        studet=input("Enter your details for logging of study into the file...\n")
        stu=open("study.txt","a")
        stu.write(f"{studet} \n")
        stu.close()
    elif b=="exercise" or b=="e":
        exedet=input("Enter your details for logging of exercise into the file...\n")
        exe=open("exercise.txt","a")
        exe.write(f"{exedet} \n")
        exe.close()
    elif b=="food" or b=="f":
        fooddet=input("Enter your details of food for logging into the file separated into commas...\n")
        p=fooddet.split(",")
        for i in p:
            l.append(i)
            foo=open("food.txt","a")
        foo.write(f"{l} \n")
        foo.close()
    else:
        print("You have given the wrong input")

def retrieve():
    b=input("What do you want to retrieve, if you want to retrieve for Study Enter 'study' or 's', if you want to retrieve for Exercise Enter 'exercise' or 'e', if you want to retrieve for food Enter 'food' or 'f'\n")
    if b=="study" or b=="s":
        stu=open("study.txt","r")
        print(stu.read())
        stu.close()
    elif b=="exercise" or b=="e":
        exe=open("exercise.txt","r")
        print(exe.read())
        exe.close()
    elif b=="food" or b=="f":
        foo=open("food.txt","r")
        print(foo.read())
        foo.close()
    else:
        print("You have given the wrong input")

while True:
    a=int(input("Press 0 if you want to log the details, Press 1 if you want to see the details\n"))
    if a==0:
        log()
    elif a==1:
        retrieve()
    else:
        print("You have given the wrong input")
