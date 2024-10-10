list_task = []

def create():
    user_input = input("ENTER THE TASK OR PRESS ENTER TO EXIT: ")
    while user_input != "":
        list_task.append(user_input)
        user_input = input("ENTER THE TASK OR PRESS ENTER TO EXIT: ")

def print_list():
    if not list_task:
        print("THE LIST IS EMPTY")
        return

    for index, task in enumerate(list_task):
        print(f" {index} --> {task}")

def update():
    if not list_task:
        print("THE LIST IS EMPTY")
        return

    print_list()
    index = int(input("ENTER THE INDEX OF THE TASK THAT YOU WANT TO UPDATE: "))        
    if 0 <= index < len(list_task):
        list_task[index] = input("ENTER THE NEW TASK: ")
    else:
        print("INVALID INDEX")

def delete():
    if not list_task:
        print("THE LIST IS EMPTY")
        return

    print_list()
    index = int(input("ENTER THE INDEX OF THE TASK THAT YOU WANT TO DELETE: "))        
    if 0 <= index < len(list_task):
        del list_task[index]
    else:
        print("INVALID INDEX")

def choices():
    print("ENTER 1 to create a task")
    print("ENTER 2 to print the list")
    print("ENTER 3 to update a task")
    print("ENTER 4 to delete a task")
    print("ENTER 0 to exit")

choices()
choice = int(input("ENTER YOUR CHOICE: "))
while choice != 0:
    if choice == 1:
        create()
    elif choice == 2:
        print_list()
    elif choice == 3:
        update()
    elif choice == 4:
        delete()
    else:
        print("INVALID CHOICE")

    choices()
    choice = int(input("ENTER YOUR CHOICE OR 0 TO EXIT: "))