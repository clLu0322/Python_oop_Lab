import add_stu, del_stu, modify_stu, print_all

def main():
    ## NOTE: NO if else elif judgements are allowed in the main function !!!!

    student_list = read_student_file()
    select_result = 0

    while select_result != 4:
        select_result = print_menu()

        try:
            {0: add_stu.main, 1: del_stu.main, 2: modify_stu.main, 3: print_all.main}[select_result](student_list)
        except:
            pass

    restore_student_file(student_list)

def read_student_file():
    student_list = list()
    try:
        with open("student_list.txt", "r") as fp:
            student_list = [eval(line.strip()) for line in fp]
    except Exception:
        print('read file error, create new empty file')
        pass
    return student_list

def restore_student_file(student_list):
    # restore student list to file here
    with open("student_list.txt", "w") as fp:
        for line in student_list:
            fp.write(str(line) + "\n")

def print_menu():
    print()
    print("0. Add a student's name and score")
    print("1. Delete a student")
    print("2. Modify a student's score")
    print("3. Print all")
    print("4. Exit")
    selection = int(input("Please select: "))

    return selection

main()