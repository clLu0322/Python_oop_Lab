def quiz3():
    value = int(input('Please enter a odd number: '))
    while (value % 2 == 0):
        value = int(input('Please enter a odd number: '))
    for i in range(1, value + 1, 2):
        print(' ' * ((value - i) // 2) + '*' * i)
    for j in range(1, value, 2):
        print(' ' * ((j // 2) + 1) + '*' * (value - j - 1))
