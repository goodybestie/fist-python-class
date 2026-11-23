'''
Data Structure
1. Introduction To Lists
1. list are ordered, mutable collections of item
2. They can contain items of different data types

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

# fruits = ['mango', 'apple', "fruit"]
# print(fruits[0:2])


# print(fruits)

#modifying list
fruits = ['mango', 'apple', "fruit", 'watermelon']
fruits[1]= "banana"
print(fruits)
#list method
fruits.append('orange') #append add an item
# fruits.insert(1, "watermelon")
fruits.remove('mango') #removing the first occurence of an item
# print(fruits)

#remove and return the last item
popped_fruits = fruits.pop()
# print(popped_fruits)
# print(fruits)

fruit_indexed = fruits.index('watermelon')
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

#list comprehension
lst = []
for x in range(10):
    lst.append(x**2)
    print(lst)