# Daily Discipline & Income Builder CLI
# Full version: Create plan, View tasks, Mark done, Daily streak

# Initialize today plan and streak
today_plan = {}
streak = 0

def show_plan(plan):
    """Print the goal and tasks with status"""
    print("\nYour current plan:")
    print("Goal:", plan["goal"])
    for i, task in enumerate(plan["tasks"], start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i}. {task['task']} - {status}")

def check_all_done(plan):
    """Return True if all tasks are done"""
    return all(task["done"] for task in plan["tasks"])

while True:
    print("\n--- Daily Discipline & Income Builder ---")
    print("1. Create Today Plan")
    print("2. View Tasks")
    print("3. Mark Task Done")
    print("4. Daily Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Create Today Plan
        today_plan = {}
        today_plan["goal"] = input("Enter your goal for today: ")

        tasks = []
        for i in range(1, 4):
            task_name = input(f"Enter task {i}: ")
            tasks.append({"task": task_name, "done": False})

        today_plan["tasks"] = tasks

        print("\nYour plan for today created successfully!")
        show_plan(today_plan)

    elif choice == "2":
        # View Tasks
        if today_plan:
            show_plan(today_plan)
        else:
            print("No plan created yet.")

    elif choice == "3":
        # Mark Task Done
        if today_plan:
            show_plan(today_plan)
            try:
                choice_task = int(input("Enter task number to mark as done: "))
                if 1 <= choice_task <= len(today_plan["tasks"]):
                    today_plan["tasks"][choice_task - 1]["done"] = True
                    print(f"Task {choice_task} marked as done!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No plan created yet.")

    elif choice == "4":
        # Daily Summary & Streak
        if today_plan:
            show_plan(today_plan)
            if check_all_done(today_plan):
                streak += 1
                print(f"\nCongratulations! All tasks done today! Your streak is {streak} day(s).")
            else:
                print("\nYou have incomplete tasks today. Keep going!")
        else:
            print("No plan created yet.")

    elif choice == "5":
        print("Exiting... Keep hustling!")
        break

    else:
        print("Invalid choice")
