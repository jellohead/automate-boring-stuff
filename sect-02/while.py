spam = 0
while spam < 5:
    print('Hello world! ' + str(spam + 1))
    spam = spam + 1

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thanks!')


spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))
