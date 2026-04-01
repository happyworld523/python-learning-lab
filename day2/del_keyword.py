a=b=3
del a
print(a) #NameError: name a is not defined
print(b)  #cannot because of the error above, but if we comment out the line above, it will print 3, which means that del only deletes the variable name, not the value.