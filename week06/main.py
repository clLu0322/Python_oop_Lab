from AddStu import AddStu
from PrintAll import PrintAll
from client_demo import SocketClient

host = "127.0.0.1"
port = 20001
socket = SocketClient(host,port)

def main():
    action_list = {"add": add, "show": show}
    select_result = "initial"
    while select_result != "exit":
        select_result = print_menu()
        try:
            action_list[select_result]()
        except Exception as e:
            print(e)

def print_menu():
    print()
    print("add: Add a student's name and score")
    print("show: Print all")
    print("exit: Exit")
    selection = input("Please select: ")
    return selection

def add():
    parameters = AddStu().execute()
    socket.send_command('add', parameters)
    raw_data = socket.wait_response()
    print(f"    The client receive data => {raw_data}")
    if raw_data['status'] == 'OK':
        print(f"    Add {parameters} success")
    else:
        print(f"    Add {parameters} fail")

def show():
    socket.send_command('show', {})
    raw_data = socket.wait_response()
    print(f"    The client receive data => {raw_data}")
    stu_info = raw_data["parameters"]
    PrintAll().execute(stu_info)   

if __name__ == '__main__': 
    main()