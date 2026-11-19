## Variables in Python
# introduction to variables in Python
# declaring and assigning variables
# naming conventions for variables (name should be descriptive, must always start with a letter or an _, can contain letters, NUMBERS, and underscores )
# understanding variables types
# type checking and conversion
# dynamic typing in Python

age = 25
height = 5.9
name = "Alice"
is_student = True

print("Age:", age)


#valid variables
first_name = "John"
last_name = "Doe"
#invalid variables


#understanding variable types
#python is dynamically typed, type of variable is determined by the runtime value assigned to it

name = "Alice"  # string

#type checking and conversion
#type checking
age = 25
type(age)

#type conversion
age_str = str(age)
print(age_str)
print(type(age_str))

name="krish"
int(name)

height = 3.4
type(int(height))

#dynamic typing in Python
#python allows the variable to change as the program executes
var = 10
print(type(var))  

var = "Hello"
print(type(var))

#input
age=int(input("Enter your age: "))
print("Your age is:", age, type(age))

#simple calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2
multi = num1 * num2
diff = num1 - num2
div = num1 / num2

print("Sum:", sum)
print("Product:", multi)
print("Difference:", diff)
print("Quotient:", div)