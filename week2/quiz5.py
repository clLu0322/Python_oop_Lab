import random

def quiz5():
    answer = random.randint(0, 101)
    high = 100
    low = 0
    guess = int(input(f"Please guess a number from {low} to {high}: "))
    limit_cnt = 1
    while (guess != answer and limit_cnt <= 6):
        if guess > answer:
            high = guess
        else:
            low = guess

        guess = int(input(f"Please guess a number from {low} to {high}: "))
        while (guess <= low or guess >= high):
            guess = int(input(f"Please guess a number from {low} to {high}: "))
        limit_cnt +=1

    if answer == guess:
        print('You passed')
    else:
        print('Achieve limited')

        
        
            



