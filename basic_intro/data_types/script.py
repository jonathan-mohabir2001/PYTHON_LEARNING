# In this python file I will be covering some data types, variables, string contatencation, data type casting, and 
# String formatting. 
x = 34 
y = 32
z = x+y 
# above are three variables, first two are assigned INTEGER types 
# last variable is assigned an addition operation which adds x and y together. 
print(z)
# z is then printed out to the console. 
float1 = 243.34
float2 = 210.23
# Floats are data types which contain decimal points at the end. 
subtractFloat = float1 - float2
print(subtractFloat) 
# the subtract float variable is assigned a subtraction operation of the two float values previously declared. 
# the output is then printed. 

#String data types below 
message = "Hello there" 
# a variable is assigned a string that has a greeting. 
name = "Jonathan Mohabir"
# My name assigned to the name variable 
greeting = message + " " +name
# the greeting variable is contatenating two strings previously declared. This is done using the + operator. 
print(greeting)

print(str(23))
# This print out statement is converting the int value of 23 to a string 
print( float(23))
# This print out statement converts the int value of 23 into a float 
print(int(234.009))
# This print out statement is converting the float value of 234 into an int 

#Formatting strings will be practised below: 
print(f"This statement will format my name to all upercase{name.upper()}")
# the statement above is using a string formatting option which takes the string value of name and turns all letters to uppercase
print (f"Here is a formatted math operation: {(12.344 + 23.344):0.2f}")
# this formatting statement formats the addition operation output to two decimal places