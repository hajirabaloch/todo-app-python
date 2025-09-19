print("=== TO-DO APP STARTING ===")
print("Welcome to your To-Do List!")

todo_list = []

def add_todo():
    print("\n=== Add New Todo ===")
    title = input("Enter todo title: ")
    date = input("Enter date (e.g., 2025-09-19): ")
    todo_list.append({"title": title, "date": date})
    print("Todo added successfully!")

def view_todos():
    print("\n=== Your Todos ===")
    if len(todo_list) == 0:
        print("No todos yet!")
    else:
        for i, todo in enumerate(todo_list, 1):
            print(f"{i}. {todo['title']} - {todo['date']}")

def delete_single_todo():
    print("\n=== Delete Single Todo ===")
    if len(todo_list) == 0:
        print("No todos to delete!")
        return
    view_todos()
    try:
        choice = int(input("Enter the number of todo to delete: "))
        if 1 <= choice <= len(todo_list):
            removed = todo_list.pop(choice - 1)
            print(f"Deleted todo: {removed['title']}")
        else:
         print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_all_todos():
    print("\n=== Delete All Todos ===")
    if len(todo_list) == 0:
        print("No todos to delete!")
        return
    confirm = input("Are you sure you want to delete all todos? (yes/no): ")
    if confirm.lower() == 'yes':
        todo_list.clear()
        print("All todos deleted!")
    else:
        print("Deletion canceled.")

def main():
    while True:
        print("\n" + "="*30)
        print("1. Add todo")
        print("2. View todos")
        print("3. Delete single todo")
        print("4. Delete all todos")
        print("5. Exit")
        print("="*30)
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            add_todo()
        elif choice == "2":
            view_todos()
        elif choice == "3":
            delete_single_todo()
        elif choice == "4":
            delete_all_todos()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__== "__main__":
    main()