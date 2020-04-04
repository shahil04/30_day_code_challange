#Number operations and comments
#number operations(ints,floats,basic math ,number weirder operations,commnents type,
#documentation  overview QA section

#day 2
# variables and data type 
# in python their are majior 3 type of  data type use
# 1.)int
# 2.)float
# 3.)str

print(type(1)) #int
print(type(234398479437498374389478932474824794234479341)) #int

print(type(1.003))#float
print(type(134777469876478169387276.95879575757589)) #float

print(type('a')) #string


print(type("a")) #string
print(type('demo')) #string 


# in python not the concept of char datatype
# their are no any concept of long ,double types of datatype.



# Numbers and Math
# Symbol 	Name
# + 	Addition
# - 	Subtraction
# * 	Multiplication
# / 	Division
# ** 	Exponentiation
# % 	Modulo
# // 	Integer Division

# commonly used math operators
print("maths operations")
print("add")
print(4+5)
print(4+(-5))

print("subtract")
print(9-5)
print(-9-6)

print("multiply")
print(4*8)
print(0.487438*(-1))

print("divide")
print(10/3)
print(20/2)
print(int(20/2))

print("power(exponential)")
print(2**3)
print(3**(-0.5))

print("integer devision")
print(10//3)
print(21//2)

print("module--->reminder show")
print(10%3)
print(21%2)


# VARIABLE ASSIGNMENT

x = 100
tom,ands,jarry=2,3,4
dragons = 1
fire=2.00323
print(dragons+x)
print(x+fire)
print(tom+ands+jarry)
y='ram'
#print(dragons+y) # this line show error because of datatype are diffrent so we change them into 1datatype
print(str(dragons)+y)
#print(dragons+int(y)) 
print("""    note ----> all data type into string 
                       but sting does not change into any other data type 
                       so when you work in diffrent datatype you change into 
                       one datatype format """)

#101 
#Variables are always assigned with the variable name on the left and the value on the right of the equals sign.

#                              Naming Restrictions
                    # 1. Variables must start with a letter or underscore
                    # 2. The rest of the name must consist of letters, numbers, or underscores
                    # 3. Names are case-sensitive

# In Python, you can name your variables whatever you want, with some restrictions:




#                                          Data Types

                # Python data types include:
                # data type 	description

                # bool 	        True or False values
                # int 	        an integer (1, 2, 3)
                # str        	(string) a sequence of Unicode characters, e.g. "Colt" or "程序设计"
                # list 	        an ordered sequence of values of other data types, e.g. [1, 2, 3] or ["a", "b", "c"]
                # dict       	a collection of key: values, e.g. { "first_name": "Colt", "last_name": "Steele" }
#=============================================================================================================

# Python is highly flexible about reassigning variables to different types:
# Dynamic Typing

awesomeness = True
print(awesomeness) # True

awesomeness = "a dog"
print(awesomeness) # a dog

awesomeness = None
print(awesomeness) # None

awesomeness = 22 / 7
print(awesomeness) # 3.142857142857143

# We call this dynamic typing, since variables can change types readily.
# Declaring Strings
# String Escape Characters
# We call this dynamic typing, since variables can change types readily.

#===================================================================================================


#                                    Declaring Strings

#           String literals in Python can be declared with either single or double quotes.
str_type_1='this is single quote string'
str_type_2="it is double quote string"
str_type_3="""it is trible quote string.
              it is use for multiple line print 
              in a multiple line."""
# Either one is perfectly fine; but make sure you stick to the same convention throughout the same file.

#============================================================================================ 


#                                        String Concatenation

#                        Concatenation is combining multiple strings together. 
#                        In Python you can do this simply with the "+" operator.

str_one = "your"
str_two = "face"
str_three = str_one + " " + str_two  # your face

#                        You can also use the "+=" operator!

#===================================================================================


#                                      Formatting Strings

#          There are also several ways to format strings in Python to interpolate variables.

#                    The new way (new in Python 3.6+) => F-Strings

x = 10
formatted = "I've told you {x} times already!"

#                The tried-and-true way (Python 2 -> 3.5) => .format method

x = 10
formatted = "I've told you {} times already!".format(x)

#                    The old way => % operator (deprecated)

#===================================================================================
# how to use comment line in python use only #---them write your comment

print("""*.) So nderstand how to assign and use variables
*.) Learn Python variable naming restrictions and conventions
*.) Learn and use some of the different data types available in Python
*.) Learn why Python is called a dynamically-typed language
*.) Understand how to convert data types
*.) Learn the ins and outs of Strings!
*.) Build a silly little program that gets user input""")