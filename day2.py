#                                               day 2
#                                     booleaN and conditional logic
# ===============================================================================
# User Input
name=input("enter your name\n")
print("your name is "+name)

# ======================================
#      boolean expression
print(type(name)==str) #true
 
 #if value is right then answer will true otherwise fales
print(1==4)# false



#           Truthiness

x = 1
x is 1  # True
x is 0  # False
#============================================================================
#             Conditional Statements



#           Conditional Checks

if name == "Arya":
    print("Valars")
elif name == "Jonson":
    print("You know nothing")
else:
    print("Carry on bro!")


#======================================================


#                           Comparison Operators
# Op 	What it does 	                                Example

# == 	Truthy if a has the same value as b            	a == b  # True
# != 	Truthy if a does NOT have the same value as b 	a != b  # False
# >     Truthy if a is greater than b                   a > b  # False
# < 	Truthy if a is less than be b                   a < b  # False
#  	
# 
# >=    Truthy if a is greater than or equal to b        a >= b  # True
# <= 	Truthy if a is less than or equal to b           a <= b  # True

#+========================================================================


# Logical Operators
# Op 	    What it does 	                                        Example

# and 	Truthy if both a AND b are true (logical conjunction)    	if a and b:
#                                                                   print(c)
# or 	    Truthy if either a OR b are true (logical disjunction) 	if am_tired or is_bedtime:
#                                                                   print("go to sleep")
# not 	Truthy if the opposite of a is true (logical negation)  	if not is_weekend:
#                                                                   print("go to work")

#=========================================================================================


print("_______________________________is vs. '=='______________________")                              

#  In python, "==" and "is" are very similar comparators, however they are not the same.

a = 1
a == 1  # True
a is 1  # True

a = [1, 2, 3]  # a list of numbers
b = [1, 2, 3]
a == b  # True
a is b  # False

c = b
b is c  # True

# "is" is only truthy if the variables reference the same item in memory

#+=================================================
print("____________________________For loops_______________________________")

#    In Python, for loops are written like this:
itembox=[1,5,3,7]
for item in itembox:
    print(item)

print("______________range use in for loop____________")
for i in range(1,10):
    print(i)

    # item references the current position of our iterator within the iterable.
    #  It will iterate over (run through) every item of the collection and 
    #  then go away when it has visited all items

    # item is a new variable that can be called whatever you want

    # An iterable object is some kind of collection of items, 
    # for instance: a list of numbers, a string of characters, a range, etc.

#-+==========================================================
print("_________________________while loop______________________")

#    We can also iterate using a while loop, which has a different format:

while (1==1):#  this loop going until the condiotion will false
    print('i love you')

# while loops continue to execute while a certain condition is truthy, and will end when they become falsy.

# while loops require more careful setup than for loops, since you have to specify the termination conditions manually.



#Controlled Exit

while True:
    command = input("Type 'exit' to exit: ")
    if (command == "exit"):
        break   #this is keyword to break the loop if if condition is true
#======================================================================================
