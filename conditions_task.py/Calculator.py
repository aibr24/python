#Ask for two numbers.
#Check if numbers. if not print the numbers were invalid
#if numbers, check op and print answer. if not op print op not valid
#end
#


print("Beep. Boop.")
print("I will be your calculator this evening.")
n1 = int(input("Please enter the first number.: "))
n2 = int(input("Please enter the second number.: "))
op = input("Please enter the operation you would like to conduct.(+,-,/,*): ")
cb = (n1,n2)



def operation(n1,n2,op):
	if op == '+':
		return n1 + n2
	elif op == '-':
		return n1 - n2
	elif op == '/':
		return n1 / n2
	elif op == '*':
		return n1 * n2
	else:
		return "The operand or number you entered was invalid."
print(operation(n1,n2,op))


'''Sidenote: Couldnt get the number function to work even when using the same format as the operand check condition
so I went with the int() condition on the input 
unitl i can learn why i couldt get it to work later'''