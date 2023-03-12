num=int(input("How many inputs you want to give\n"))
list=[]
for i in range(1,num+1):
	inp=int(input("Give your inputs\n"))
	list.append(inp)
print("Press 1 for list comprehension, Press 2 for Dictionary comprehension, Press 3 for Set Comprejension", "Press 4 for Generator Comprehension")
t=int(input())
if t==1:
	ls=[i for i in list]
	print(ls)
	print(type(ls))
elif t==2:
	dict={i:f"{i} is good boy" for i in list}
	print(dict)
	print(type(dict))
elif t==3:
	set={item for item in list}
	print(set)
	print(type(set))
elif t==4:
	gen=(item for item in list)
	print(gen.__next__())
	print(type(gen))
	for i in gen:
		print(i)

else:
	print("Invalid input")

	