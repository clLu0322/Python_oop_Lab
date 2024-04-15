
class AddStu:
    def __init__(self):
        self.parameters = {'name': "", 'score': {}}

    def execute(self):
        name = input("  Please input a student's name or exit: ")
    
        if name == 'exit':
            return self.parameters
        
        self.parameters['name'] = name

        while True:

            subject = input("  Please input a subject name or exit for ending: ")

            while subject in self.parameters['score'].keys():
                print(f"    {subject} is already exists")
                subject = input("  Please input a subject name or exit for ending: ")

            if subject == 'exit':
                break
            
            while True:
                try:
                    score = float(input(f"  Please input {name}'s {subject} score or < 0 for discarding the subject: "))
                    if score < 0:
                        break
                    self.parameters['score'][subject] = score
                    break   
                except Exception as e:
                    print(e)
                    pass
                
        return self.parameters
    