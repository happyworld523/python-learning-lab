# Variable assignment in Python can be done in a single line, allowing you to assign values to multiple variables at once. This is a convenient way to initialize several variables with different values in a concise manner.
a, b, c = 1, 2.4, 'Hello, World!'
print(a, b, c)

# Multiple variables can be assigned the same value in a single line:
a=b=c= 100
print(a, b, c)

# swapping values of two variables can be done in a single line without the need for a temporary variable:
x = 10
y = 20
x, y = y, x
print("After swapping: x =", x, "y =", y)