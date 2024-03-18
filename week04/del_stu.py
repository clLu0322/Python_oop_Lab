def main(student_dict):
    while True:
        name = input("  Please input a student's name or exit: ")
        if name == 'exit':
            return
        if name not in student_dict.keys():
            print(f"    The name {name} is not found")
            return
        del student_dict[name]
        print(f"    Del {name} success")












