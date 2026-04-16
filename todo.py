import json
import os

def add_tasks():
   print("what task?")
   new_task = input()
   tasks.append({"id" : len(tasks)+1, "work" : new_task, "done" : False})
   print("successful!")

def refresh_id():
    for i in range(0,len(tasks)):
        tasks[i]["id"] = i+1

def show_task():
    if not tasks:
        print("no task here")
        return
    for task in tasks:
        status = "✓" if task["done"] else "✗"
        print(f'id {task["id"]} task:{task["work"]} done:{status}')

def toggle_task(id):
    for task in tasks:
        if task["id"] == id:
            task["done"] = not task["done"]
            print(f'{task["work"]}: status changed')
            return
    print("that task doesn't exist")

def delete_task(id):
    for task in tasks[:]:
        if task["id"] == id:
            tasks.remove(task)
            refresh_id()
            print("task deleted!")
            return
    print("that task doesn't exist")

base_dir = os.path.dirname(os.path.abspath(__file__))

json_path = os.path.join(base_dir, "data.json")

with open(json_path, "r") as data:
    tasks = json.load(data)


while True:
    print("What do you want to do enter the number | Show:1, Add:2, Toggle:3, Delete:4")
    
    command = input()
    if command == "1":
        show_task()

    elif command == "2":
        add_tasks()

    elif command == "3":
        id = int(input("id?"))
        toggle_task(id)

    elif command == "4":
        id = int(input("id?"))
        delete_task(id)
    
    else:
        print("again")
    print("\n")
    with open(json_path, "w") as data:
        json.dump(tasks, data, indent=4)