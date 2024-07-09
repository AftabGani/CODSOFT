tasks=[]

def addTask():
    task=input("Task to be added:")
    tasks.append(task)
    print(task,"has been added in the list.")

def deleteTask():
    viewTask()
    try:
        if tasks:
            taskToDelete = int(input("Choose the number of the task you want to delete: "))
            if taskToDelete <= len(tasks) and taskToDelete > 0:
                deleted_task = tasks.pop(taskToDelete - 1)
                print(f"Task '{deleted_task}' has been deleted from the list.")
            else:
                print("Invalid task number")
        else:
            print("Empty List")
    except ValueError:
        print("Invalid Input.")

def UpdateTask():
    viewTask()
    try:
        if tasks:
            taskToUpdate = int(input("Choose the number of the task you want to update: "))
            if 1 <= taskToUpdate <= len(tasks):
                updatedTask = input("Enter the updated task: ")
                tasks[taskToUpdate - 1] = updatedTask
                print(f"Task '{updatedTask}' has been updated in the list.")
            else:
                print("Invalid task number.")
        else:
            print("Empty List")
    except ValueError:
        print("Invalid Input.")

def viewTask():
    if not tasks:
        print("Empty List")
    else:
        for index, task in enumerate(tasks):
            print(index+1,".",task)

if __name__=="__main__":
    print("TO-DO LIST")
    while True:
        print("Choose the option to be performed:")
        print("-----------------------------------")
        print("1. Add a new task")
        print("2. Delete an existing task")
        print("3. Update a task")
        print("4. View a task")
        print("5. Exit")

        choice=input("Your Choice:[1/2/3/4]")

        if choice=='1':
            addTask()
        elif choice=='2':
            deleteTask()
        elif choice=='3':
            UpdateTask()
        elif choice=='4':
            viewTask()
        elif choice=='5':
             break
        else:
            print("Wrong Input..")
    print("Exiting...")
        
