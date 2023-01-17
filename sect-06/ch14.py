# Ch 14 for loops with lists, multiple assignment, and
# augmented operators

supplies = ['pens', 'staplers', 'tools', 'desk', 'computer']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# multiple assignment
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print(size)
print(color)
print(disposition)

# variable swapping
a = 'AAA'
b = 'BBB'
a, b = b, a
print(a)
print(b)


# augmented assignment operators
spam = 42
spam = spam + 1
spam += 1  # this works with most math operators + - * / %
print(spam)

catLength = len(cat)
print(catLength)
print(len(cat))
