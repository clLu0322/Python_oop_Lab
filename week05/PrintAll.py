class PrintAll:
    def __init__(self, student_dict):
        self.student_dict = student_dict
    
    def execute(self):
        print ("\n==== student list ====\n")
        for index, value in self.student_dict.items():
            print(f"Name: {index}")
            for subject, score in value.items():
                print(f"  subject: {subject}, score: {score}")
                print()
        print ("======================")
        return self.student_dict
