def main(student_dict):
    name = input("  Please input a student's name or exit: ")
    while name not in student_dict.keys():
        print(f"    {name} is not exists")
        name = input("  Please input a student's name or exit: ")

    if name == 'exit':
        return
    
    subject_list = " ".join(student_dict[name].keys())
    print(f"  current subjects are {subject_list}")
    change_subject = input("  please input the subject you want to change: ")

    if change_subject not in student_dict[name].keys():
        score = float(input(f"  Add a new subject for {name} please input {change_subject} score or < 0 for discarding the subject: "))
        if score < 0:
            return
        else:
            student_dict[name][change_subject] = score
            print("    Add successfully")
            return

    while True:
        try:
            change_score = float(input(f"  Please input {name}'s new score of {change_subject}: "))
            student_dict[name][change_subject] = change_score
            print(f" Modify [{name}, {change_subject}, {change_score}] success")
            break
        except Exception as e:
            print(e)
    
 

































