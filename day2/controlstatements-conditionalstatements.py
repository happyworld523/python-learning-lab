#Example 1
age=15
if age>=18: # () is optional in Python, but it is a good practice to use it for better readability and to avoid errors when we have multiple conditions.
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#Example 2
num=4
if num%2==0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")

#Example 3
if True:
    print("This is true.")
else:
    print("This is false.")

#Example 4
if False:
    print("This is true.")
else:
    print("This is false.")

#Example 5
if 0:
    print("This is true.")
else:
    print("This is false.")

#Example 6    
if 1:
    print("This is true.")
else:
    print("This is false.")


#Ternary operator - also known as conditional expression - is a one-line if-else statement that assigns a value to a variable based on a condition. The syntax is: variable = value_if_true if condition else value_if_false
age=20
status = "Adult" if age >= 18 else "Minor"
print("You are an", status) #You are an Adult - because the condition age >= 18 is true, so the value "Adult" is assigned to the variable status. If the condition were false, the value "Minor" would be assigned to status instead.

age=20
print("You are an", "Adult" if age >= 18 else "Minor")
print("You are an Adult") if age >= 18 else print('minor')

#Multiple print statements in ternary operator
age=20
{print('adult'), print("You are an Adult")} if age >= 18 else {print('minor'), print("You are a Minor")}

#multiple conditions using elif - also known as else if - allows us to check multiple conditions in a sequence. The syntax is: if condition1: ... elif condition2: ... else: ...
weekno = 1

if (weekno == 1):
    print("Monday")
elif weekno == 2:
    print("Tuesday")
elif (weekno == 3):
    print("Wednesday")
elif weekno == 4:
    print("Thursday")
elif weekno == 5:
    print("Friday")
elif weekno == 6:
    print("Saturday")
elif weekno == 7:
    print("Sunday")