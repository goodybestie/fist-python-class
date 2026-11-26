#conditional statement (if, elif, else)
#introduction to conditional statements
#if statement
#else statement
#elif statement
#nested condional statements
#practical examples

'''
"Conditional logic is used to make decisions" is correct. Here are other ways to define it, from simple to more technical. Different ones will click for different students.

Simple definitions
"Conditionals let a program choose what to do based on whether something is true or false."
"A conditional runs a piece of code only when a condition is met."
"Conditionals let a program do different things in different situations."
"Conditionals control which path the program takes."
'''

#if statement evaluate a condition and execute the block of code within it.  if the condition is true. If the condition is false, it skips the block of code.
# age = 18
# if age >= 18:
#     print("You are eligible to vote.")

#else statement is used to execute a block of code when the condition in the if statement is false.
#elif statement is used to check multiple conditions. It allows you to specify additional conditions to be checked if the previous conditions are false.

# age = 18
# if age < 18:
#     print("You are not eligible to vote.")
# elif age == 18:
#     print("You are eligible to vote.")


# name = 13
# print(name)

x=True
y = False

if y:
    print(y) 
else:
    print('wrong conditional logic')

#nested conditional statements are used when you have multiple conditions that need to be checked within each other. It allows you to create more complex decision-making structures.
