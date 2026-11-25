##single line comment   
##basic syntax of python
#case sensitive

##multiline comment
'''
basic syntax of python
- case sensitive
'''

name = 'Goody'
Name =  'Goodys'
# print(name)


#python indentation is important
# a = 10
# b = 20
# if a < b:
#     print('a is less than b')

#     #line continuation is done with a backslash (\) 
#     a=1+2+3+4+5+6+7+8+9+10\
#     +11+12+13+14+15
#     print(a)

# length = 13
# width = 5
# area = length + width
# print("Area of rectangle is:", area)

#declaring and assigning variables
# age = 25
# name = "Alice"
# height =5.9
# is_student = True

#naming conventions for variables

# first_name = "John"
# second_name = "Doe"
# print(first_name + " " + second_name)

#understanding variable types
age = 25
name = "Alice"
height =5.9
is_student = True

# print(type(age))
# print(type(name))
# print(type(height))
# print(type(is_student))

# type checking and conversion
age ="25"
# print(type(age))
# print (type(int(age)))

#dynamic typing in Python
# variable = int("10")
# print(type(variable))

# age = 25
# gender = input("Enter your Gender: ")
# print(type(gender))


'''
2. Creating Lists
3. Accessing List Elements
4. Modifying List Elements
5. List Methods
6. Slicing Lists
7. iterating over lists
8.  list comprehensions
9.  Nested Lists
'''
#creating list
lst = [1, 'hello', 1.5, True]
# print(lst)
students_name=['Goodness', 'inyene', 'samuel', 'Goodnews']
# print(students_name)

# print(students_name[-1])
# print(students_name[1:])
# print(students_name[1:3])
# print(students_name[::-1])

#modifying list elements
# students_name[0]="Goody"
# print(students_name)

#list method
# students_name.append('chris') #add an item to the end
# print(students_name)

# students_name.insert(0,'emma') #you add an item to any specific position
# print(students_name)

# num=[1,2,3,4,5,6,7,8,9,10, 10]
# num.sort()
# print(num)

# num.reverse()
# print(num)

# num.remove(5)
# print(num)

# num.index(2)
# print(num.index(10))
# print(num.count(10))
# num.pop(5)
# print(num)
# print(num)

#slicing list
'''
Summary
Slice	        Meaning      Result for nums
nums[2:6]	index 2 up to 6	[2, 3, 4, 5]
nums[:3]	first 3	[0, 1, 2]
nums[::2]	every 2nd item	[0, 2, 4, 6, 8]
nums[1::2]	every 2nd, starting at 1	[1, 3, 5, 7, 9]
nums[::-1]	reversed	[9, 8, 7, ... 0]
nums[:]	everything (a copy!)	[0, 1, ... 9]
'''

# num=[1,2,3,4,5,6,7,8,9,10]
# print(num[:])#gives all element
# print(num[::]) #gives all element
# print(num[:3]) #gives from 1st to third number
# print(num[2:]) #count from 3 down
# print(num[::2])#step afte each element
# print(num[6::])#count from seven down
# print(num[::-1])
# print(num[5:1:-1])

#iterating over lists
nums=[1,2,3,4,5,6,7,8,9,10]



# for student in students_name:
#     print(student)
# for student in enumerate(students_name):
#     print(student)

#with conditional logic [expression for item in iterable if condition]
# prices=[]

# for p in range(19):
#     if p > 10:
#         prices.append(p*2)
# print(prices)

prices=[2,3,4,5,6,7,8,9]

for p in prices:
    # print(p)
    if p < 10:
        prices.append(p*2)
print(prices)

#list comprehension
# lst=[]

#(basic syntax) [expression for item in iterable]

# for x in range(10):
#         lst.append(x+2)
#         # print(x)
# print(lst)


