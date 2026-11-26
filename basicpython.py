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

# prices=[2,3,4,5,6,7,8,9]

# for p in prices:
#     # print(p)
#     if p < 10:
#         prices.append(p*2)
# print(prices)

#list comprehension
# lst=[]

#(basic syntax) [expression for item in iterable]

# for x in range(10):
#         lst.append(x+2)
#         # print(x)
# print(lst)

'''
A list comprehension is a short way to create a new list by 
going through each item in a collection, 
optionally changing it and/or choosing which items to keep.
'''

items_collection = [100, 200, 300]

new_list = []
#long way

for item in items_collection:
    if item==300:
        new_list.append(item)
# print(new_list)

#shortway
#(basic syntax) [expression for item in iterable]

new_collections = [[item**2] for item in range(10) ]
# print(new_collections)


new_items=[num for num in range(10) if num==5]
# print(new_items)


'''
Level 1: Warm-up (filter)
Make a list of all scores 50 and above (passed).
Make a list of all scores below 50 (failed).
'''
'''
Level 2: Transform
The teacher adds 5 bonus marks to everyone. Make a new list of the updated scores.
Make a list of all the names in UPPERCASE.
'''

# grades=["A", "C", "F"]


# scores = [50, 60, 70, 80, 90, 100]
# failure = [10, 20, 30, 40]
# names=['Goodness', 'Inyene', 'Goodnews', 'Samuel']



# passed =[score for score in scores if score >= 50]
# print(f"passed:{passed}")

# fail =[score for score in failure if score < 50]
# print(f"you failed:{fail}")

# bonus_mark=[score+5 for score in scores]
# print(bonus_mark)

# capital_names =[name.upper() for name in names]
# print(capital_names)

'''
Level 5: Challenge ⭐
Make a list of grades for every score, using this rule:
70 and above → "A"
50 to 69 → "C"
below 50 → "F"

Hint: you can put an if/else in the expression part: "A" if score >= 70 else ...
'''

# grades=["A"if score >= 70 else "C" if score >=50 else "F" for score in scores]
# print(grades)

#nested list
# lst = [[1, 2, 3,], ['a', 'b', 'c'], [True,False]]

#nested list comprehension
# lst1=['a', 'b', 'c']
# lst2=[1,2,3]

# pair=[[first, last]for first in lst1 for last in lst2]
# print(pair)

# total=[item for item in items_collection if item==300]
# print(total)







lst1=[1,2,3]
lst2=["a", "b", "c"]

pair=[[i, j]for i in lst1 for j in lst2]
# print(pair)


'''
1. introduction to tuples
2. creating tuples
3. accessing tuple elements
4. tuple operations
5. immutable nature of tuples
6. tuple methods
7. packing and unpacking tuples
8. nested tuples

'''

#introduction to tuples
'''
tuple are ordered collections of items that are immutable.
they are similar to lists, but their immutability makes them different.
'''

items=('hello','world','True',"how", 'when', 'hello')

# print(items.count('hello'))
# print(items.index('when'))


# items[0]='ready'

# num=(1,2,3,4,5)

#tuples operation
# concantinate_operation= items + num
# print(concantinate_operation)

# sum = concantinate_operation * 3
# print(sum)

# print(items[2])
# print(items[2:])
# print(items[::3])  #step

#packing and unpacking tuple 
#packed tuple (Packing puts several values into one tuple. )
pack_tuple= 1, "hello", True
# print(pack_tuple)
# Unpacking takes the values out of a tuple and puts each one into its own variable.
#unpacked tuple
# age, name, condition = pack_tuple
# print(age)
# print(name)
# print(condition)

#If you only want some values, 
# put * in front of one variable to collect "everything else" into a list:

# num = (1,2,3,4,5,6)
# *first, second, last = num
# print(first)
# print(second)
# print(last)

'''

Data Structure
1. Introduction To dictionary
1. dictionaries are unordered collections of items. they store data in key-value pairs.
Keys must be unique and immutable(e.g, strings, numbers, or tuples), while values can be any type.

2. They can contain items of different data types

2. Creating dictionay
3. Accessing dictionary Elements
4. Modifying dictionary Elements
    dictionary method
5. iterating over dictionaries
6.  Nested dictionary

'''

#creating dictionary



# students["school"]="Futurelabs"
# print(students)
# students["age"]=30
# print(students)
students={"name":"Goodness", "age":35, "country":"Nigeria", "beautiful":True, "height":1.5}
# print(students["country"])
# del students["height"]
# print(students)

#dictionary method
# key=students.keys()
# print(key)
# value=students.values()
# print(value)
# item=students.items()
# print(item)

#iterating over dictionaries
for key in students.keys():
    print(key)
for value in students.values():
    print(value)
for item in students.items():
    print(item)
    
#nested dictionaries
collection_students={
    "students1":{"name":"Goodness", "age":35, "country":"Nigeria", "beautiful":True, "height":1.5},
    "students2":{"name":"Goodness", "age":35, "country":"Nigeria", "beautiful":True, "height":1.5},
    "students3":{"name":"Goodness", "age":35, "country":"Nigeria", "beautiful":True, "height":1.5},
}

#iterating over student dictionary

for student_key, student_info in students.items():
    print(f" key: {student_key}, info: {student_info}")
