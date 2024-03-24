
class AddStu:
    def __init__(self, student_dict):
        self.student_dict = student_dict

    def execute(self):
        name = input("  Please input a student's name or exit: ")
        while name in self.student_dict.keys():
            print(f"    {name} is already exists")
            name = input("  Please input a student's name or exit: ")
        
        if name == 'exit':
            return
        
        self.student_dict[name] = {}
        while True:

            subject = input("  Please input a subject name or exit for ending: ")
            while subject in self.student_dict[name].keys():
                print(f"    {subject} is already exists")
                subject = input("  Please input a subject name or exit for ending: ")

            if subject == 'exit':
                break
            
            while True:
                try:
                    score = float(input(f"  Please input {name}'s {subject} score or < 0 for discarding the subject: "))
                    if score < 0:
                        break
                    self.student_dict[name][subject] = score
                    break
                except Exception as e:
                    print(e)
                    pass

        return self.student_dict
    