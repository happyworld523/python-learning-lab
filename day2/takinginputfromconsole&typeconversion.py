num1 = input("Entering number 1: ")
num2 = input("Entering number 2: ")
print("The sum of", num1, "and", num2, "is", num1 + num2) #The sum of 10 and 20 is 1020 - because the input() function returns a string, so num1 and num2 are strings, and the + operator performs string concatenation instead of addition.

# to perform addition, we need to convert the input strings to numbers using the int() function for integers or the float() function for floating-point numbers.
num1 = int(float(input("Entering number 1: "))) #The int() function is used to convert the input string to an integer, and the float() function is used to convert the input string to a floating-point number. This allows us to handle cases where the user might enter a decimal number, which would cause an error if we tried to convert it directly to an integer.
num2 = int(input("Entering number 2: "))
print("The sum of", num1, "and", num2, "is", num1 + num2) #The sum of 10 and 20 is 30 - because num1 and num2 are now integers, so the + operator performs addition.

num1 = float(input("Entering number 1: "))
num2 = float(input("Entering number 2: "))
print("The sum of", num1, "and", num2, "is", num1 + num2) #The sum of 10 and 20 is 30 - because num1 and num2 are now integers, so the + operator performs addition.
