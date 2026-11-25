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
7. dictionary comprehensions

'''

is_dis={}
# print(type(is_dis))

#single key is always used

my_dist={'name':"Goodness", "age":28, "height":1.5, "name":"goody"} #replace value and consider it has one key
# print(my_dist)

#easiest way to access dictionary element
# print(my_dist['name'])

#accessing dictionary element using dictionary get method
# print(my_dist.get('name'))/

#modifying dictionary element
#dictionary are mutable so you can add, update and delete.

my_dist["age"]= 24 #update the key value
my_dist['country']='nigeria' #add a new key and value pair
# del my_dist['name']  #delete key and value pair
# print(my_dist)

#dictionary method
# keys = my_dist.keys()
# print(keys)
# value=my_dist.values()
# print(value)
# items=my_dist.items()
# print(items)

#iterating over dictionary
#you can use loops to iterate over dictionaries, keys, values and items.

# for key in my_dist.keys():
#     print(key)
# for value in my_dist.values():
#     print(value)
# for key, value in my_dist.items():
#     print(f"{key}: {value}")

#nested dictionaries
students = {
   "students1":{'name':"goodness", "age":25, 'country':"nigeria"},
   "students2":{'name':"joel", "age":26, 'country':"nigeria"}
}
# print(students)

# print(students["students1"]['name'])
# print(students["students1"]['age'])

#iterating over students dictionaries

for student_id,students_info in students.items():
    print(student_id, students_info)
    for key,value in students_info.items():
        print(f'{key}:{value}')