while True:
    print("\n--- Daily Discipline & Income Builder ---")
    print("1. Create Today Plan")
    print("2. View Tasks")
    print("3. Mark Task Done")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Create plan selected")
    elif choice == "2":
        print("View tasks selected")
    elif choice == "3":
        print("Mark task selected")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
