from AddStu import AddStu
from ModifyStu import ModifyStu
from DelStu import DelStu
from PrintAll import PrintAll
from SocketClient import SocketClient

def main():
    socket = SocketClient()
    action_list = {
                    "add": AddStu,
                    "del": DelStu,
                    "modify": ModifyStu,
                    "show": PrintAll               
                    }
    select_result = "initial"
    while select_result != "exit":
        select_result = print_menu()
        try:
            action_list[select_result](socket).execute()
        except Exception as e:
            print(e)

def print_menu():
    print()
    print("add: Add a student's name and score")
    print("del: Delete a student")
    print("modify: Modify a student's score")
    print("show: Print all")
    print("exit: Exit")
    selection = input("Please select: ")
    return selection

main()