Name = 'Chandra'
age = 28
salary = 50000.21

#1
print("#1-----------------------")
print('Name:', Name)  #adds space after the comma
print('Age:', age)
print('Salary:', salary)

#2
print("#2-----------------------")
print('Name:' + Name) #Name:Chandra - No space, because the + operator concatenates the string 'Name:' with the value of the variable Name, which is 'Chandra'.
print('Age:'+ str(age)) #Age:28 - No space, because the + operator concatenates the string 'Age:' with the string representation of the variable age, which is '28'. We need to convert age to a string using the str() function, because we cannot concatenate a string with an integer directly.
print('Salary:' + str(salary)) #Salary:50000.21 - No space, because the + operator concatenates the string 'Salary:' with the string representation of the variable salary, which is '50000.21'. We need to convert salary to a string using the str() function, because we cannot concatenate a string with a float directly.

#3
print("#3-----------------------")
print("Name: %s, Age: %d, Salary: %g" %(Name, age, salary)) #Name: Chandra, Age: 28, Salary: 50000.2 - The %s format specifier is used for strings, %d is used for integers, and %g is used for floating-point numbers. The values of the variables Name, age, and salary are inserted into the string in the order they are provided in the tuple after the % operator.

#4
print("#4-----------------------")
print("Name: %s Age: %d Salary: %2.2f" %(Name, age, salary)) #Name: Chandra, Age: 28, Salary: 50000.21 - The %s format specifier is used for strings, %d is used for integers, and %2.2f is used for floating-point numbers with 2 decimal places. The values of the variables Name, age, and salary are inserted into the string in the order they are provided in the tuple after the % operator.
#what is 2.2f? - The 2 before the decimal point indicates the minimum width of the field, and the .2 after the decimal point indicates that we want to display 2 digits after the decimal point. If the number has fewer than 2 digits after the decimal point, it will be padded with zeros. If it has more than 2 digits after the decimal point, it will be rounded to 2 decimal places.

#5
print("#5-----------------------")
print("Name: {}, Age: {}, Salary: {}".format(Name, age, salary)) #Name: Chandra, Age: 28, Salary: 50000.21 - The {} placeholders are used to indicate where the values of the variables should be inserted into the string. The values of the variables Name, age, and salary are provided as arguments to the format() method in the order they should be inserted into the string.

#6
print("6-----------------------")
print("Name: {0}, Age: {1}, Salary: {2}".format(Name, age, salary)) #Name: Chandra, Age: 28, Salary: 50000.21 - The {0}, {1}, and {2} placeholders are used to indicate where the values of the variables should be inserted into the string. The values of the variables Name, age, and salary are provided as arguments to the format() method in the order they should be inserted into the string. The numbers inside the curly braces indicate the position of the argument in the format() method.

#7
print("#7-----------------------")
print("Name: {name}, Age: {age}, Salary: {salary}".format(name=Name, age=age, salary=salary)) #Name: Chandra, Age: 28, Salary: 50000.21 - The {name}, {age}, and {salary} placeholders are used to indicate where the values of the variables should be inserted into the string. The values of the variables Name, age, and salary are provided as keyword arguments to the format() method, where the names of the arguments correspond to the placeholders in the string.

#8
print("#8-----------------------")
print(f"Name: {Name}, Age: {age}, Salary: {salary}") #Name: Chandra, Age: 28, Salary: 50000.21 - The f before the string indicates that it is an f-string, which allows for inline expressions. The values of the variables Name, age, and salary are inserted into the string at the positions of the curly braces {}. The expressions inside the curly braces are evaluated at runtime and their values are inserted into the string.

