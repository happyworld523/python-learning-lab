#range function is used to generate a sequence of numbers
# it takes three arguments: start, stop, and step  
# start is the first number in the sequence (inclusive) - default is 0
# stop is the last number in the sequence (exclusive) - required
# step is the difference between each number in the sequence (default is 1)

#Example 1: Generate a sequence of numbers from 0 to 9
print(range(10)) #range(0, 10) - because the default start is 0, and the stop is 10, so the range function generates a sequence of numbers from 0 to 9.
print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - because the range function generates a sequence of numbers from 0 to 9, and the list() function converts the range object to a list.
print(list(range(0, 10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - because the start is 0, the stop is 10, and the step is positive (default is 1), so the range function generates a sequence of numbers from 0 to 9.
print(list(range(0, 10, 2))) #[0, 2, 4, 6, 8] - because the start is 0, the stop is 10, and the step is 2, so the range function generates a sequence of numbers from 0 to 8 with a step of 2.
print(list(range(0, 10, -1))) # why it is empty list? - because the start is 0, the stop is 10, and the step is negative (-1), so the range function cannot generate any numbers in that range, resulting in an empty list.

#Example 2: Generate a sequence of numbers from -10 to -1
print(list(range(-10))) #why it is empty list? - because the default start is 0, and the stop is -10, so the range function generates a sequence of numbers from 0 to -9, but since the step is positive (default is 1), it cannot generate any numbers in that range, resulting in an empty list.
print(list(range(-10, 0))) #[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1] - because the start is -10, the stop is 0, and the step is positive (default is 1), so the range function generates a sequence of numbers from -10 to -1.

#Example 3: Generate a sequence of numbers from -5 to -10
print(list(range(-5, -10))) # why it is empty list? - because the start is -5, the stop is -10, and the step is positive (default is 1), so the range function cannot generate any numbers in that range, resulting in an empty list.
print(list(range(-5, -10, -1))) #[-5, -6, -7, -8, -9] - because the start is -5, the stop is -10, and the step is negative (-1), so the range function generates a sequence of numbers from -5 to -9.


#Example 4: Generate a sequence of numbers from 10 to 0
print(list(range(10, -1, -1)))

#Example 5: Generate a sequence of even numbers from 2 to 10 not including 10, and a sequence of odd numbers from 1 to 10 not including 10
print(list(range(2, 10, 2))) #list of even numbers from 2 to 8 - because the start is 2, the stop is 10, and the step is 2, so the range function generates a sequence of even numbers from 2 to 8.
print(list(range(1, 10, 2))) #list of odd numbers from 1 to 9 - because the start is 1, the stop is 10, and the step is 2, so the range function generates a sequence of odd numbers from 1 to 9.