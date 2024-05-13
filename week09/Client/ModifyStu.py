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