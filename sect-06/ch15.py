# Ch 15 List methods

spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')  # returns 0

spam.index('heyas')  # returns 3

# append() and insert() are list methods and only work on list values
spam.append('moose')
print(spam)

spam.insert(2, 'goodbye')
print(spam)

# remove() removes first instance of specific list value
spam.remove('hi')
print(spam)

# sort() sorts list values as long as value data types are the same
# sort is ASCII-betical so upper-case take order precidence.

spam = [2, 5, -4, -2, 10]
spam.sort()
print(spam)

spam = ['tree', 'car', 'house', 'toy']
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)

# to force in true aphabetical order
spam.sort(key=str.lower)
