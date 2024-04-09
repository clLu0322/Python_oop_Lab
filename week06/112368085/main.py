from AddStu import AddStu
from PrintAll import PrintAll
import SocketClient as Client

action_list = {
    "add": AddStu, 
    "show": PrintAll
}

"""
add: exit->sent_data
show: sent_data->PrintAll
剩add
"""
def main():
    client = Client.SocketClient(Client.host, Client.port)
    select_result = "initial"

    while select_result != "exit":
        select_result = print_menu()
        try:
            action_list[select_result](client).execute()
        except Exception as e:
            print(e)


def print_menu():
    print()
    print("add: Add a student's name and score")
    print("show: Print all")
    print("exit: Exit")
    selection = input("Please select: ")

    return selection

main()