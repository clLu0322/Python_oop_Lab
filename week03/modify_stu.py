def main(student_list):
    name = input("  Please input a student's name: ")
    find_name = False
    
    try:
        for i in student_list:
            if i[0] == name:
                new_score = float(input(f"  Please input {name} new score: "))
                i[1] = new_score
                find_name = True

        if find_name:
            print(f"  Modify [{name}, {new_score}] success")
        else:
            print(f"  The name {name} is not found")
    except ValueError:
        print("Invalid input! Please enter a valid score as a number.")
