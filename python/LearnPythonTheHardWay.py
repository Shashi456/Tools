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


#To use command line arguments you can use argv
from sys import argv
script, filename = argv
print(script)
#f = open(file=filename) - > returns a file object
#open(file='<name',mode=) , various modes like r,w,rw,r+,w+,a available
#The file operator has its own functions like read, write, seek etc.
# Other functions with files include close , readline, truncate.
#Some more file operations
from os.path import exists
#There exist other functions like os.path.join() etc
print(exists(filename))


# Some pointers about functions :
def acc2(*args):
    a1, a2 = args
    print(a1, a2)
def acc2v2(a1, a2):
    print(a1, a2)
#Above are the two ways to accept multiple arguments
#The first one is convenient in case of handling extreme cases
#The default arguments always fall on the left


#Remember about truthy and falsy values in Logic
#It's very important to check for the above while writing programs
#Python returns one of the operands to their boolean expressions rather
#than just True or False. This means that if you did False and 1
#, then you get the first operand (False), but if you do
#True and 1, then you get the second (1).
