'''
Randomness and acummulator pattern.
Part 1
The idea
Normally a program gives the same answer every time you run it:
Randomness lets a program give a different, unpredictable answer each time, like rolling a dice or flipping a coin.
That's really all randomness is: a function that hands you an unpredictable number.

Part 2: The accumulator pattern
The idea

An accumulator is just a variable that keeps a running total while a loop runs.

Part 3: Put them together

Now combine both ideas: roll a dice 5 times and add up all the rolls.
'''
import random;

# roll = random.randint(1, 6)
# print(roll)

total = 0

for i in range(5):
    roll = random.randint(1, 6)
    total +=roll
    print(total)


# Coin counter: flip a coin (randint(0, 1)) 10 times. Count how many heads (1s) you get.

# coin = 0
# for i in range(10):
#     flip = random.randint(0, 1)
#     print(flip)
#     if flip == 1:
#         coin = coin + 1
# print(f'heads: {coin}' )

# heads = 0

# for i in range(10):
#     count = random.randint(0, 1)
#     # print(count)
#     if heads == 1:
#         heads = heads + 1
# print(f"total: {heads}")

#accumulator
# dice = 0

# for day in range(5):
#     dice = dice + 100
#     print(dice)


'''
Try these yourself
Coin counter: flip a coin (randint(0, 1)) 10 times. Count how many heads (1s) you get.
Savings: start with ₦0 and add ₦500 each week for 4 weeks. Print the total each week.
Two dice: roll two dice 3 times and print the total of each pair.
'''

# import random

# heads = 0

# for i in range(10):
#         counter = random.randint(0, 1)
#         print(counter)
#         if counter ==1:
#             heads=heads +1

# savings = 0

# for i in range(4):
#         savings = savings +500
#         print(savings)  


# dice = 0
# for i in range(3):
#         dice1 = random.randint(1, 6)
#         dice2 = random.randint(1, 6)
#         sum = dice1 + dice2
#         dice = dice + sum
#         print(dice)