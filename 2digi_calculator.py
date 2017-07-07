def main():
	print("Welcome to this basic 2 digit calculator app. All you have to do is provide 2 digits and whether you want to add, subtract, multiply, or divide.")
	num1 = int(input("Please enter the first digit: "))
	op = input("For additiong type 'a' \nFor subtraction type 's' \nFor multiplication type 'm' \nFor division type 'd' \nPlease enter which operation you wish to use: ")
	num2 = int(input("please enter the second digit: "))

	if op == 'a':
		print(add(num1,num2))
	elif op == 's':
		print(sub(num1,num2))
	elif op == 'm':
		print(mul(num1,num2))
	elif op == 'd':
		print(div(num1,num2))
	else:
		print("Invalid operation.")
		main()



def add(num1, num2):
	result = num1 + num2
	return result

def sub(num1, num2):
	result = num1 - num2
	return result

def mul(num1, num2):
	result = num1 * num2
	return result

def div(num1, num2):
	result = num1 / num2
	return result

main()
