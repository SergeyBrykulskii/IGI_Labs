from storage import Storage
import os


def input_command() -> tuple:
    input_text = input("Enter command:   ").split(" ", 1)

    command = input_text[0]
    args = []

    if len(input_text) > 1:
        args = input_text[1]

    return command, args


def is_save_file(current_storage: Storage):
    while True:
        ans = input("Do you want to save storage to file?(y/n):   ")
        if ans == 'y':
            current_storage.save()
            break
        if ans == 'n':
            break
        
    

def execute_comand(command_name: str, command_arguments: str, current_storage: Storage):
    match command_name:
        case 'switch':
            if not command_arguments:
                print('Enter user name')
                return
            is_save_file(current_storage)
            current_storage.switch(command_arguments)
            print(f"Current user is {command_arguments}")
       
        case 'add':
            if command_arguments:
                elems = command_arguments.split()
                for el in elems:
                    current_storage.add(el)
            
        case 'remove':
            if command_arguments:
                current_storage.remove(command_arguments)

        case 'grep':
            res = current_storage.grep(command_arguments)
            if len(res) != 0:
                print('Found values: ' + str(res))
            else:
                print('No such element')

        case 'find':
            if current_storage.find(command_arguments):
                print(command_arguments)
            else:
                print('No such element')

        case 'save':
            current_storage.save()
        
        case 'list':
            print(current_storage.list())

        case 'load':
            current_storage.load(command_arguments)


        case _:
            print('Unidentified command')


def main():
    user_name = input('Enter your name:  ')
    current_storege = Storage(user_name)
    print(f'Welcome, {user_name}')

    while True:
        command, args = input_command()
        if command == 'exit':
            break
        execute_comand(command, args, current_storege)


if __name__ == "__main__":
    main()

