# A different way of printing (The comma works as concatenation)
# print("what's up" , 5 > 2 )


# String formatting
# Strings can be printed with help of escape sequences as well
a = 40
# the following f is for formatting the strings
# the {} -> is for mentioning the variable
#print(f"I am {a} years old.")
b = 50
#Two ways of formating, the .format is more readable
print(f"How do you know {a} + {b} is 90?")
print("How do you know {} + {} is 90?".format(a,b))
print("How do you know %i + %i is 90?" %(a,b))
# the parameters after % needs to be in a tuple


# end is the delimiter, default newline , can be changed
# but changing it always can be cumbersome
print("Good", end = ' ')
print("Morning")


from sys import argv
f,s,t = argv
print(f)
print(s)
print(t)
