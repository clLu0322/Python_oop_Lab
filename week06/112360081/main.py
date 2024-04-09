import client
import threading

from AddStu import AddStu
from PrintAll import PrintAll

ACTION_LIST = {
    "add": AddStu, 
    "show": PrintAll
}

def main():
    ## NOTE: NO if else elif judgements are allowed in the main function !!!!

    client_main = client.SocketClient(client.HOST, client.PORT)
    student_dict_temp = dict()
    select_result = "NULL"

    while select_result != "exit":
        select_result = print_menu()
        try:
            action_status = ACTION_LIST[select_result]().execute(client_main)
        except Exception as e:
            print(e)

def print_menu():
    print()
    print("add: Add a student's name and score")
    print("show: Print all")
    print("exit: Exit")
    selection = str(input("Please select: "))

    return selection

main()