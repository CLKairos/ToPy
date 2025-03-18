from datetime import date

taskNumber = 1
todoArray = []
startedArray = []
finishedArray = []

def save(list, filename):
    with open(filename, "w") as file:
        for task in list:
            file.write(f"{task}\n") 
    if debug:
        print(f"Saved to {filename}")
        print(list)

def addtask():
    global taskNumber
    task = str(input("What do you need to do? "))
    dueMonth = int(input("What Month is it Due? "))
    dueDay = int(input("What Day is it Due? "))
    dueYear = int(input("What Year is it Due? "))
    finalString = str(f"{taskNumber}: {task}: {dueMonth}-{dueDay}-{dueYear}")
    todoArray.append(finalString)
    save(todoArray, "todo.txt")
    taskNumber += 1

def starttask():
	readtasks(1, 2)
	taskinp = int(input("What task do you want to start? "))
	if taskinp <= len(todoArray):
		startedArray.append(todoArray.pop(taskinp - 1)) 
		save(todoArray, "todo.txt")
		save(startedArray, "started.txt")
	else:
		print("Task not found!")

def finishtask():
	readtasks(2, 3)
	taskinp = int(input("What task do you want to finish? "))
	if taskinp <= len(startedArray):
   		finishedArray.append(startedArray.pop(taskinp - 1)) 
   		save(startedArray, "started.txt")
   		save(finishedArray, "finished.txt")
	else:
   		print("Task not found!")

def readtasks(selectionA, selectionB):
    if selectionA == 1 or selectionA == 4:
        print("Todo List:")
        for task in todoArray:
            print(task)
    if selectionB == 2 or selectionA == 2 or selectionA == 4:
        print("Started List:")
        for task2 in startedArray:
            print(task2)
    if selectionB == 3 or selectionA == 4:
        print("Finished List:")
        for task3 in finishedArray:
            print(task3)
    else:
        print("No tasks available.")

def load_tasks():
    global todoArray, startedArray, finishedArray, taskNumber
    try:
        with open('todo.txt', 'r') as file:
            todoArray = file.read().splitlines()
        with open('started.txt', 'r') as file:
            startedArray = file.read().splitlines()
        with open('finished.txt', 'r') as file:
            finishedArray = file.read().splitlines()
        if todoArray:
            taskNumber = len(todoArray) + 1  
    except FileNotFoundError:
        print("No previous tasks found, starting fresh.")

def cleartasks():
    global todoArray, startedArray, finishedArray, taskNumber
    todoArray = []
    startedArray = []
    finishedArray = []
    taskNumber = 1
    save(todoArray, "todo.txt")
    save(startedArray, "started.txt")
    save(finishedArray, "finished.txt")
    print("All tasks have been cleared!")

def debug():
    print(taskNumber)
    print(todoArray)
    print(startedArray)
    print(finishedArray)

def start():
    load_tasks()
    
    while True:
        try:
            inpt = int(input("1 for read | 2 for add | 3 to start task | 4 to finish task | 5 to clear all tasks: "))
            if inpt == 1:
                readtasks(4, 0)
            elif inpt == 2:
            	addtask()         
            elif inpt == 3:
                starttask()
            elif inpt == 4:
           		finishtask()
           	elif inpt == 5:
           		cleartasks()
            elif inpt == 6:
                debug()
            else:
                print("Invalid Code")
        except ValueError:
            print("Incorrect Input")

start()
