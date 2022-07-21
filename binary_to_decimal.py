# binary to decimal python code

numeral = list(input("Enter the binary number: "))
result = 0

for i in range(len(numeral)):
	digit = numeral.pop()
	if digit == '1':
		result = result + pow(2, i)
print("The decimal result of the number is", result)

# End of the program