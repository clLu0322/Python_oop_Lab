class PrintAll:
    def __init__(self):
        pass
    def execute(self, client_main):
        try:
            client_main.send_command('show', {})
            data = client_main.wait_response()
            print(f"The client received data => {data}")
            student_dict = data["parameters"]
        except Exception as e:
            print(e)
        try:
            print("\n==== student list ====\n")
            for i, j in student_dict.items():
                print('Name:{}'.format(i))
                for k, l in j.items():
                    print('   subject: {},score:{}'.format(k, l))
                print()
            print ("======================")

        except Exception as e:
            print(e)
          