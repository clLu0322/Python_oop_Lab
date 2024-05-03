class PrintAll:
    
    def __init__(self, socket):
        self.socket = socket
        self.socket.send_command("show", {})
        self.student_dict = self.socket.wait_response()["parameters"]

    def execute(self):
        print ("\n==== student list ====\n")
        for index, value in self.student_dict.items():
            print(f"Name: {index}")
            for subject, score in value['scores'].items():
                print(f"  subject: {subject}, score: {score}")
            print()
        print ("======================")
