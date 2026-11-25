'''
sets are a built-in data type in python used to storecollections of unique items. 
They are unordered, meaning that the elements do not follow a specific order,
and they do not allow duplicate elements. sets are useful for membership tests, eliminating duplicate entries 
and performing mathematical set of operations like union, intersection, difference, and symmetric difference.

'''

#creating set
# my_set={1, 2, 3, 4}
# print(type(my_set))

# empty_set=set([1, 2, 3, 4, 4, 2])
# print(empty_set)

#Basic set operation
#Adding and removing elements

# my_set.add(7)
# print(my_set)

# my_set.remove(7)
# print(my_set)

#discard element
#removing a random element using pop method

# removed_element = my_set.pop()
# print(removed_element)
# print(my_set)

#clear element
# my_set.clear()
# print(my_set)

#unordered set


#set membership test(weather an element is present in the set or not, weather an element is a member of a set or not)
# my_set={1, 2, 3, 4}/
# print(3 in my_set) #it just checking if this element is in the set
# print(7 in my_set)

#mathematical operations
# set1={1,2,3,4,5,6}
# set2={4,5,6,7,8,9}

#union operation(having a set and combining all the element) union simply means combining everything
# union_set=set1.union(set2)
# print(union_set)

#intersection (simply gives a common element from both the set i.e element that are available in both set)
# intersection_set=set1.intersection(set2)
# print(intersection_set)

# print(set1.difference(set2)) #remove common element that are present in set2
# print(set1.difference_update(set2))
# print(set1)

# symmetric difference(common element are being removed from both element i.e unique element remain)
# print(set1.symmetric_difference(set2))
# print(set1)

#set methods
set1={1,2,3}
set2={3,4,5}

#issubset
print(set1.issubset(set2))