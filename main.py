# Daily Discipline & Income Builder - Step 3

# Initialize today plan as empty
today_plan = {}

while True:
    print("\n--- Daily Discipline & Income Builder ---")
    print("1. Create Today Plan")
    print("2. View Tasks")
    print("3. Mark Task Done")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # --- Step 3: Create Today Plan ---
        today_plan = {}
        today_plan["goal"] = input("Enter your goal for today: ")

        tasks = []
        for i in range(1, 4):
            task = input(f"Enter task {i}: ")
            tasks.append(task)

        today_plan["tasks"] = tasks

        # Show the plan back to the user
        print("\nYour plan for today:")
        print("Goal:", today_plan["goal"])
        for i, task in enumerate(today_plan["tasks"], start=1):
            print(f"{i}. {task}")

    elif choice == "2":
        # Step 4 will add proper View Tasks
        if today_plan:
            print("\nYour current tasks:")
            print("Goal:", today_plan["goal"])
            for i, task in enumerate(today_plan["tasks"], start=1):
                print(f"{i}. {task}")
        else:
            print("No plan created yet.")

    elif choice == "3":
        # Step 4 will add marking tasks done
        print("Mark Task functionality will be added in Step 4.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
