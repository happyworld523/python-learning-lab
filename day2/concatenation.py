a=10
b=20.5
print(a+b) #30.5, because a and b are numbers, so the + operator performs addition


a=True
b=2
print(a+b) #3, because a is treated as 1 and b is treated as 2, so the + operator performs addition 

#Concatenation of two strings
a="Hello, "
b="World!"
print(a+b) #Hello, World!, because a and b are strings, so the + operator performs concatenation

a=2
b=" apples"
#print(a+b) #TypeError: unsupported operand type(s) for +: 'int' and 'str', because a is an integer and b is a string, so the + operator cannot perform addition or concatenation
print(str(a)+b) #2 apples, because a is converted to a string using the

a=False
b=True
c=" is a boolean value"
print(str(a)+ str(b) + c) #FalseTrue is a boolean value, because a and b are converted to strings using the str() function, and then concatenated with c using the + operator