import SocketClient as Client

class PrintAll:
    def __init__(self, client: Client.SocketClient):
        self.client = client

    def execute(self):
        self.client.send_command("show")
        raw_data = self.client.wait_response()
        if raw_data["status"] == "OK":
            student_dict = raw_data["parameters"]

        print ("\n==== student list ====\n")
        for name, basic_info in student_dict.items():
            print(f"Name: {name}")
            for subject_name, score in basic_info["scores"].items():
                print(f"  subject: {subject_name}, score: {score}")
        print ("\n======================")