#introduction to loops
#for loop(iterating over a range, iterating over a string)
#while loop
#loop control statements(break,continue,pass)
#nested loops
#

#forloop is used to iterate over a sequence of number
# print(range(5))

# for i in range(5):
#     print(i)



# for i in range(1, 10, 1):
#     print(i)
#while loop is used to execute a block of code repeatedly as long as a condition is true.``
# count = 0
# while count<5:
#     print(count)
#     count=count+1

#loop control statements are used to control the flow of a loop. The break statement is used to exit a loop prematurely, the continue statement is used to skip the current iteration and move to the next iteration, and the pass statement is used as a placeholder for future code.
#nested loops are used to create a loop inside another loop. The inner loop is executed for each iteration of the outer loop.
# for i in range(3):
#     for j in range(2):
#         print(f"i:{i} and j:{j}")

for i in range(5):
    if i == 3:
        break
    print(i)
