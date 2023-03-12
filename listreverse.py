try:
    item=int(input("Enter How many Calorie Element you want to give\t"))
    cal=[]
    for i in range(1,item+1):
        d=int(input(f"Enter the No.{i} caloric Element\t"))
        cal.append(d)
except Exception as e:
    print("Enter input correctly, you might have entered string or without space")
# Slicing method to print in reverse
sli=cal[::-1]
print(sli)
# Function is used to reverse
func=cal.copy()
func.reverse()
print(func)
# Logic is used to reverse
log=cal.copy()
for i in range(item):
    log[i]=cal[item-i-1]
print(log)

k=cal[:]
for p in range(len(cal)//2):
    k[p],k[len(k)-p-1]=k[len(k)-p-1],k[p]
print(k)

try:
    if sli==func==log==k:
        print("All the methods give the same result")
except NameError:
    print("Please Enter correctly")
    