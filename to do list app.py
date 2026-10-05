tasks = [];
while True:
    print("\n--- to do list ---");
    print("1. add task");
    print("2. view tasks");
    print("3. mark task as completed");
    print("4. exit");
    choice = input("choose an option:");
    if choice == "1":
        task = input("enter task:");
        tasks.append({"task": task , "done" : False});
        print("task added");
    elif choice == "2":
        if not tasks:
            print("no taks found");
        else:
            for i , t in enumerate(tasks,1):
                status = "ok" if t["done"] else " " 
                print(f"{i}. [status] {t["task"]}");
    elif choice == "3":
        num = int(input("enter task number:"));
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True;
            print("tasks marked as completed!");
        else:
            print("invalid task number.");
    elif choice == "4":
        print("goodbye!");
        break;
    else:
        print("invalid option.");
        
