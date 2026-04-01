# Arithmetic operators in Python
a=5
b=2

print(a+b) #7
print(a-b) #3
print(a*b) #10
print(a/b) #2.5
print(a//b) #2, floor division, it gives the quotient without the remainder
print(a%b) #1, modulus operator, it gives the remainder of the division
print(a**b) #25, exponentiation operator, it gives the result of a raised to the power of b

#Relational operators in Python - also known as comparison operators - always return a boolean value (True or False)
print(a>b) #True
print(a<b) #False
print(a==b) #False
print(a!=b) #True
print(a>=b) #True
print(a<=b) #False

#Logical operators in Python - used to combine conditional statements - uses and, or, not - requires boolean values - also return a boolean value 
x=True
y=False
print(x and y) #False, because both x and y need to be true for the result to be true
print(x or y) #True, because at least one of x or y is true
print(not x) #False, because x is true, so not x is false
print(not y) #True, because y is false, so not y is true
