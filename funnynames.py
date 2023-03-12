import random
num = int(input("How many names you want to give: "))
name=[]
for i in range(1,num+1):
    name.append(input(f"Enter the Names you want to give:\n"))

fname=[]
lname=[]
def funny_names():
    for i in name:
        fname.append(i.split(" ")[0])
        lname.append(i.split(" ")[1])
    
    for j in name:
        funfname = random.choice(fname)
        fname.remove(funfname)
        funlname = random.choice(lname)
        lname.remove(funlname)
        print(funfname +" "+funlname)
funny_names()