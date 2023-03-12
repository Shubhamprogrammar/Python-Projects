print("Welcome to calculator made by shubham")
while True:
	num1 = int(input("Please enter your number1\n"))
	num2 = int(input("Please enter your number2\n"))
	print("Enter the operation"+"+,-,*,/,**")
	choice = (input("Please enter your operation\n"))
	if choice=='*':
		print(num1*num2)
	elif choice=='+':
		print(num1+num2)
	elif choice=='-':
		print(num1-num2)
	elif choice=='/':
		print(num1/num2)
	elif choice=='**':
		print(num1**num2) 				
	else:
		print("Enter correctly")
    	