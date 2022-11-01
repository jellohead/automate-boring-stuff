def spam():
    global eggs
    eggs = 'hello'
    print(eggs)


eggs = 42
print(eggs)
spam()
print(eggs)
