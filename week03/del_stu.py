def main(student_list):
    name = input("  Please input a student's name: ")
    find_name = False
    for i in student_list:
        if name == i[0]:
            student_list.remove(i)
            find_name = True
    
    if find_name == True:
        print(f"  Del {name} sucess")
    else:
        print(f"  The name {name} is not found")
