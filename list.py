'''
Data Structure
A data structure is a way of organizing data in memory so it's easy to use.

1. Introduction To Lists
1. list are ordered, mutable collections of item.
2. They can contain items of different data types.

2. Creating Lists
3. Accessing List Elements
4. Modifying List Elements
5. List Methods
6. Slicing Lists
7. iterating over lists
8.  list comprehensions
9.  Nested Lists

'''

#accessing list elements
#accessing required item

fruits = ['mango', 'apple', "fruit"]
# print(fruits[0:2]) #means "start at index 0, stop before index 2."
# print(fruits[1])


# print(fruits)

#modifying list
fruits = ['mango', 'apple', "fruit", 'watermelon']
fruits[1]= "banana"
# print(fruits)
#list method
fruits.append('orange') #append add an item to the end
# fruits.insert(1, "watermelon") add an item in a specific index
fruits.remove('mango') #removing the first occurence of an item
# print(fruits)

#remove and return the last item
popped_fruits = fruits.pop()
# print(popped_fruits)
# print(fruits)

fruit_indexed = fruits.index('watermelon') #is in what index
# print(fruit_indexed)

count_fruit = fruits.count('banana') #count how many item is in the list
# print(count_fruit)
fruits.sort()
# print(fruits) #this will sort the list in ascending order
fruits.reverse()
# print(fruits)

# fruits.clear()
# print(fruits)

#slicing list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[2:5])
# print(numbers[:5])
# print(numbers[5:])
# print(numbers[::2]) #jump two step #double colon means all the element
# print(numbers[::-1])

#iterating over list

# for number in numbers:
    # print(number)
# for index,fruit in enumerate(fruits):
#     print(index, fruit)

#list comprehension
# lst = []
# for x in range(10):
#     lst.append(x**2)
#     print(lst)
# [x**2 for x in range(10)] #what we want as the output and the type of operation we are solving

#list comprehension
#(basic syntax) [expression for item in iterable]
#with conditional logic [expression for item in iterable if condition]

#basic list comprehesion
square=[i**2 for i in range(10)]
# print(square)


#list comprehension with condition
lst = []
for i in range(10):
    if i%2==0:
        lst.append(i)
# print(lst)

even_numbers = [num for num in range(10) if num%2==0]
# print(even_numbers)

#nested list comprehension [expression for item1 in iterable1 and for item2 in iterable2]
# items1=[[1, 2, 3, 4], ['a','b','c'], [True, False]]
# print(items1)

# lst=[1,2,3]
# lst_one=["a", "b", "c"]
# pair = [[i, j] for i in lst for j in lst_one]
# print(pair)

item1=[1,2,3,4]
item2=['a','b','c','d']

pair=[[i,j] for i in item1 for j in item2]
print(pair)

items=[100, 200, 300]
prices=[]

total=[item for item in items if item==200]
prices.append(total)
print(prices)


#list comprehension for function call
# words=['hello', 'world', 'python']
# length=[len(word) for word in words]
# print(length)

#conclusion
'''
List comprehensions are a powerful and concise way to create lists in Python. 
They are syntactically compact and can replace more verbose looping constructs. 
Understanding the syntax of list comprehension will help you write cleaner and more efficient python code.
'''