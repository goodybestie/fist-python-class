'''
1. introductio to tuples
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

#creating tuple

tup=tuple()
# print(type(tup))

lst=list()
# print(type(lst))

#a list can be converted into tuples;a tuples can be converted into list.
items=tuple([1, 2, 3, 4, 5,])
# print(type(items), items)

#mixted tuple
item1 = (1, 'hello', 3.5, True)
# print(item1)

#accessing tuples
numbers=(1, 2, 3)
# print(numbers)

# print(numbers[1])

#tuple operation
continate_tuple = item1 + numbers
# print(continate_tuple)

#immutable nature of tuples
#tuples are immutable meaning element cannot be changed once assign

#tuple method(count)(index)
# print(numbers.count(2))
# print(numbers.index(2))

#packing and unpacking tuple
#packed tuple
pack_tuple = 2, "hello", True
print(pack_tuple)

#unpacked tuple
a, b, c =pack_tuple
print(a, b, c)

#nested tuples (tuples inside of tuples)

#iterating over tuples

'''
conclusion
tuples are versatile and useful in many real-world scenarios where an immutable and ordered collection of
items is required. they are commonly used in data structures, function arguments and return values, and as
dictionary keys. understanding how to leverage tuples effectively can improve the efficiency and readability of
your python code.
'''