from storage import Storage




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
            is_save_file(current_storage)
            current_storage.switch(command_arguments)
            print(f"Current user is {current_storage}")
       
        case 'add':
            if command_arguments:
                current_storage.add(command_arguments)
            
        case 'remove':
            if command_arguments:
                current_storage.remove(command_arguments)

        case 'grep':
            res = current_storage.grep(command_arguments)
            if len(res) != 0:
                print('Found values: ' + str(res))

        case 'save':
            current_storage.save()
        
        case 'list':
            print(current_storage.list())

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

