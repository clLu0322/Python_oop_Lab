
class ModifyStu:
    def __init__(self, socket):
        self.socket = socket

    def execute(self):
        self.input_name()

    def input_name(self):
        self.name = input("  Please input a student's name: ")
        self.socket.send_command("query", {"name": self.name})
        self.receive_data = self.socket.wait_response()
        
        if self.receive_data["status"] == 'OK': 
            self.show_current_subject()
            self.input_subject_score()
        else:
            print(f"\tThe name {self.name} is not found")

    def show_current_subject(self):
        print("  current subjects are: ", end="")
        for subject in self.receive_data["scores"].keys():
            print(f"{subject} ", end="")
        print()

    def input_subject_score(self):
        subject = input("  Please input a subject you want to change: ")
        
        if subject in self.receive_data["scores"].keys():
            try:
                new_score = float(input(f"Please input {subject}'s new score for {self.name}: "))
                self.receive_data['scores'][subject] = new_score
                self.send_data_to_server('modify', subject, new_score)
            except Exception as e:
                print(e)
        else:
            try:
                new_score = float(input(f"  Add a new subject for {self.name}, please input {subject}'s score or < 0 to discard the subject: "))
                self.receive_data['scores'][subject] = new_score
                self.send_data_to_server('add', subject, new_score)
            except Exception as e:
                print(e)

    def send_data_to_server(self, command, subject, score):
        send_data = {'name': self.name, 'scores': self.receive_data['scores']}
        self.socket.send_command("modify", send_data)
        if self.socket.wait_response()['status'] == 'OK':
            print(f"{command.capitalize()} [{self.name}, {subject}, {score}] success")
        else:
            print(f"{command.capitalize()} [{self.name}, {subject}, {score}] fail")
        

                



"""

  Please input a student's name: Test2
    The client sent data => {'command': 'query', 'parameters': {'name': 'Test2'}}
    The client received data => {'status': 'OK', 'scores': {'Python': 11.0}}
  current subjects are Python 

  Please input a subject you want to change: Eng
  Add a new subject for Test2 please input Eng score or < 0 for discarding the subject: 100
    The client sent data => {'command': 'modify', 'parameters': {'name': 'Test2', 'scores_dict': {'Python': 11.0, 'Eng': 100.0}}}
    The client received data => {'status': 'OK'}
    Add [Test2, Eng, 100.0] success
---------------------------------------------------------------------------------------------------------------------------------------------

  Please input a student's name: Test3
    The client sent data => {'command': 'query', 'parameters': {'name': 'Test3'}}
    The client received data => {'status': 'Fail', 'reason': 'The name is not found.'}
    The name Test3 is not found
----------------------------------------------------------------------------------------------------------------------------------------------

  Please input a student's name: Test2
    The client sent data => {'command': 'query', 'parameters': {'name': 'Test2'}}
    The client received data => {'status': 'OK', 'scores': {'Python': 11.0, 'Eng': 100.0}}
  current subjects are Python Eng 

  Please input a subject you want to change: Python
  Please input Python's new score of Test2: 19
    The client sent data => {'command': 'modify', 'parameters': {'name': 'Test2', 'scores_dict': {'Python': 19.0, 'Eng': 100.0}}}
    The client received data => {'status': 'OK'}
    Modify [Test2, Python, 19.0] success

"""