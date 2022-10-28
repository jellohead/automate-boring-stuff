name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('Hey! You are not Alice!')
elif age > 2000:
    print('You are so old!')
print('Done')

print('Enter a name.')
name = input()
if name:
    print('Thanks for entering a name ' + name)
else:
    print("You didn't enter a name")
