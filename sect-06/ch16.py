# Ch 16 similarities between lists and strings

import copy
name = 'Zophie the cat'
print(name[7])
newName = name.split(' ')
print(newName)


# mutable variables save a reference, changes affect any copy since
#  any changes actually take place in the referenced list
# immutable save the value to the list
# variables contain references to lists, not the acutal list
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello'
print(cheese)
print(spam)
# cheese and spam are references to the same list


# deepcopy() creates a new copy vs providing a reference

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(cheese)
print(spam)
