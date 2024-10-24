list_task=[]
task_anjam_shode=[]
while True:
    options=int(input("enter a number"))
    match options:
        case 0:
            print("enter 1 to show list of task hay jari")
            print("enter 2 to show list of task hay anjam shode")
            print("enter 3 to add task to list jari")
            print("enter 4 to select task from list jari and move it to list anjam shode")
            print("enter 0 to show the menue")
            print("enter 5 to exit")


        case 1:
            print(list_task)
        case 2:
            print(task_anjam_shode)
        case 3:
            tasks=int(input("how many task do you want to add"))
            for i in range (tasks):
                c=input("type your task")
                list_task.append(c)
                print(list_task)
        case 4:
            done_item=int(input("choose the item you have done"))
            done=done_item-1
            task_anjam_shode.append(list_task[done])
            list_task.pop(done)
        case 5:
            break
        case _:
            print("invailid number")
