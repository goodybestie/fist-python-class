# syntax and semantics of Python programming language
## Basic Syntax for a Python Program
# case sensitive
# indentation is important
# line continuation is done with a backslash (\)

# print("Hello, World!")

# name = 'Goody'
# Name =  'Goodie'
# print(name)
# print(Name)

# age = 30
# if 30 > 20:
    # print('30 is greater than 20')


    ## understanding the semantics of Python programming language
    # variables assignment
    # type inference
    # a = 10
    # print(type(a))

    # name error

    # name = "John"
    # print(
    #     "Hello, " + name + "!")
    

    #operators
    #arithmetic operators(addtion, subtraction, multiplication, division, modulus, exponentiation, floor division)

a = 10
b = 3
sum = a + b


# print(sum)


#comparison operators(equal to,not equal to,greater than,less than,greater than or equal to,less than or equal to)

# c = 10
# d = 20
# result = c != d
# print(result)

# age = 30
# year = 40
# result = age >= year
# print(result)

# age = 30
# year = 40
# result = age <= year
# print(result)


#logical operator
#And OR Not

# x=True
# y=True
# print(x and y)

x = True
y = True
# print( x or y)

x = False
# print(not x)


# first_name =input('enter your first name')
# second_name= input('enter your second name')
# print(first_name + " " + second_name)


#loop control statement(break, continue and pause statement)

# for i in range(5):
#     if i == 3:
#         pass      #it exit a loop prematurely
#     print(i)

#continue statement  (it skips the current iteration and move to the next iteration)
# pass statement does nothing

'''
Randomness and acummulator pattern.
Part 1
The idea
Normally a program gives the same answer every time you run it:
Randomness lets a program give a different, unpredictable answer each time, like rolling a dice or flipping a coin.
That's really all randomness is: a function that hands you an unpredictable number.
'''

# print('man')


# roll = random.randint(1, 100)
# print(roll)

# Coin counter: flip a coin (randint(0, 1)) 10 times. Count how many heads (1s) you get.

heads = 0

# for i in range(10):
#     count = random.randint(0, 1)
#     # print(count)
#     if count == 1:
#         heads = heads + 1
#         print(heads)

'''

Part 2: The accumulator pattern
The idea

An accumulator is just a variable that keeps a running total while a loop runs.
'''
pink_bag = 0

for i in range(5):
    pink_bag += 100
print(pink_bag)

# The 3 rules of an accumulator
# Create it BEFORE the loop and start it at 0 → piggy_bank = 0
# Update it INSIDE the loop → piggy_bank = piggy_bank + 100
# Use it AFTER the loop → print(piggy_bank)

'''
Part 3: Put them together

Now combine both ideas: roll a dice 5 times and add up all the rolls.
'''

# roll = 0

# for i in range(5):
#     rolls = random.randint(1, 6)
#     roll= rolls + roll
# print(roll)


'''
Try these yourself
Coin counter: flip a coin (randint(0, 1)) 10 times. Count how many heads (1s) you get.
Savings: start with ₦0 and add ₦500 each week for 4 weeks. Print the total each week.
Two dice: roll two dice 3 times and print the total of each pair.
'''
total = 0


'''
The gambler simulation, step by step
The story

A gambler has ₦50. Each round, they bet ₦1 on a coin flip:

Heads: they win ₦1 (money goes up by 1)
Tails: they lose ₦1 (money goes down by 1)

They keep playing until one of two things happens:

they reach ₦100, so they've doubled their money and they stop happy
they reach ₦0, so they're broke and have to stop


# The question: how often does a gambler go broke?

Run it a few times. You'll see either Won! Money: 51 or Lost! Money: 49.


Step 2: keep betting until broke or ₦100

Now we need a loop. But which kind?

for is for when you know how many times: "flip 10 times".
while is for when you repeat until something happens: "keep betting until broke or rich".
'''
import random

money = 50
went_broke = 0

while money > 0 and money < 100:
    flip = random.randint(0,1)
    if flip == 1:
        money = money + 1
        print(f"you won: {money} congrat")
    else:
        money = money -1
        went_broke += 1
        print(f"you loss: {money}")



