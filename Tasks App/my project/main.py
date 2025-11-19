tasks = []
print('Welcome')
while True:
    print('1. Add Task')
    print('2. View Tasks')
    print('3. Delete Task')
    print('4. Exit')
    choice = input('Enter your choice: ')
    choice = int(choice)
    if choice == 1:
        value = (input('Enter your task: '))
        tasks.append(value)
        print('👍Task added')
    elif choice == 2:
        if not tasks:
            print('No tasks yet')
        else:
            print('your tasks:')
            x = 0  
            for task in tasks:
                x+=1
                print(x,task)     
    elif choice == 3:
        if not tasks:
            print('No tasks to delete')
        else:
            x = 1
            print('yout tasks:')
            for task in tasks:
                print(x,task)
                x+=1
            task_number = input('Enter your task to delete: ')
            task_number = int(task_number)
            print(f'{task_number} is deleted')
    elif choice == 4:
        print('you leaved')
        break        

            







