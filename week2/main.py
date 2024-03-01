import quiz1, quiz2, quiz3, quiz4, quiz5

def main():
    keep_going = 'y'
    while keep_going == 'y':
        print("1. Print double triangle\n"
              "2. Print spacing triangle\n"
              "3. Print diamond\n"
              "4. Print grid\n"
              "5. Guessing game")
        sel = int(input('Please select: '))

        if sel == 1:
            quiz1.quiz1()
        elif sel == 2:
            quiz2.quiz2()
        elif sel == 3:
            quiz3.quiz3()
        elif sel == 4:
            quiz4.quiz4()
        else:
            quiz5.quiz5()
        
        keep_going = input('Try again (y)?')

main()

        
    