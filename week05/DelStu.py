class DelStu:
    def __init__(self, student_dict):
        self.student_dict = student_dict
    
    def execute(self):
        while True:
            name = input("  Please input a student's name or exit: ")
            if name == 'exit':
                return self.student_dict
            if name not in self.student_dict.keys():
                print(f"    The name {name} is not found")
                return self.student_dict
            del self.student_dict[name]
            print(f"    Del {name} success")
        return self.student_dict
