
class AddStu:
    def __init__(self):
        self.student_dict = dict()
        
    def execute(self, client_main):
        name = input("  Please input a student's name or exit: ")
        score=0
        if name == "exit":
            return False

        else:
            self.student_dict['name'] = name
            self.student_dict['scores'] = dict()

            subject = input("  Please input a subject name or exit for ending: ")
            while subject!="exit":
                while True:
                    try: 
                        score = float(input(f"Please input {name}'s {subject}  or < 0 for discarding the subject:"))
                        if score>=0:
                            self.student_dict['scores'][subject] = score
                            print(f"   Add {name}'s scores successfully")
                        break
                    except:
                        print(f"Wrong format with reason could not convert string to float: '{score}', try again")       
            
                subject = input("  Please input a subject name or exit for ending: ")     

        try:       
            client_main.send_command('add', self.student_dict)
            data = client_main.wait_response()
            print(f"The client received data => {data}")
            if data['status'] == 'OK':
                print(f"Add {self.student_dict} success")
            else:
                print(f"Add {self.student_dict} fail")         
        except Exception as e:
            print(e)





















