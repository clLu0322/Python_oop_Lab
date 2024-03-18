def main(student_dict):
    name = input("  Please input a student's name or exit: ")
    while name in student_dict.keys():
        print(f"    {name} is already exists")
        name = input("  Please input a student's name or exit: ")
    
    if name == 'exit':
        return
    
    student_dict[name] = {}
    while True:

        subject = input("  Please input a subject name or exit for ending: ")
        while subject in student_dict[name].keys():
            print(f"    {subject} is already exists")
            subject = input("  Please input a subject name or exit for ending: ")

        if subject == 'exit':
            break
        
        while True:
            try:
                 score = float(input(f"  Please input {name}'s {subject} score or < 0 for discarding the subject: "))
                 if score < 0:
                    break
                 student_dict[name][subject] = score
                 break
            except Exception as e:
                 print(e)
                 pass
    
    




















