
# Python is dynamically typed, which means that you do not need to declare the type of a variable when you create it.

'''
Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
'''

#It is important to note that Python is a dynamically typed language,
# which means that you do not need to declare the type of a variable when you create it. 
# The type of a variable is determined at runtime based on the value assigned to it. 
# For example:

x = 10          # x is an integer
y = 3.14        # y is a float
name = "Alice"   # name is a string
name2 = 'Bob'
character = 'A'  # character is a string of length 1
character2 = "B"  # character2 is a string of length 1
is_valid = True  # is_valid is a boolean
print(type(x))        # Output: <class 'int'>
print(type(y))        # Output: <class 'float'> 
print(type(name))     # Output: <class 'str'>
print(type(name2))    # Output: <class 'str'>
print(type(character)) # Output: <class 'str'>
print(type(character2)) # Output: <class 'str'>
print(type(is_valid)) # Output: <class 'bool'>


x = "Hello, World!"  # x is now a string
print(type(x))        # Output: <class 'str'>