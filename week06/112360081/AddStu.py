import client
import time 

class AddStu:
    def __init__(self):
        self.student_dict = dict()
    
    def execute(self, input_client):
        name = input('Please input a student name or exit: ')
        if name == 'exit':
            return False
        else:
            self.student_dict['name'] = name
            self.student_dict['scores'] = dict()

        while True:
            try:
                while True:
                    subject = input('Please input a subject name or exit for ending: ')
                    if subject == 'exit':
                        break
                    try:                 
                        score = input('Please input ' + name + ' score or < 0 for discarding the subject: ')
                        score = float(score)
                        if score < 0:
                            continue
                        else:
                            self.student_dict['scores'][subject] = score
                    except Exception as e:
                        print(e)
        
                input_client.send_command_data('add', self.student_dict)
                
                input_client.wait_server()

                if input_client.raw_data["status"] == "OK":
                    print('add ',self.student_dict, 'success')
                    return
                else:
                    print('add ',self.student_dict, 'fail')
                    return
                
            except Exception as e:
                print(e)
    
