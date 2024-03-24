def quiz1():
    value = int(input("Please enter a value: "))
    for i in range(value, 1, -1):
        print('*' * i)
    for j in range(1, value+1):
        print('*' * j)
