import csv

to_do_list = ["study","read","clean"]

def add_one_task(title):
    to_do_list.append(title)

def print_list(todo_list):
    for index,item in enumerate(todo_list):
        print(f"{index} - {item}")

def delete_task(number_to_delete):
    to_do_list.pop(number_to_delete)

def save_todos(todo_list):
    with open("todos.csv", mode= "w", newline= "", encoding= "utf-8") as file:
        writer=csv.writer(file)
        for task in todo_list:
            writer.writerow([task])

def load_todos(route, todo_list):
    try:
        with open(route, mode= "r", newline= "", encoding= "utf-8") as file:
            reader=csv.reader(file)
            for row in reader:
                todo_list.append(row[0])
    except FileNotFoundError:
        print(f"File {route} not found. Starting with empty list.")
    return todo_list

def main():
    load_todos("todos.csv", to_do_list)
    while True:
        print_list(to_do_list)
        action = input("Choose an action: add, delete, save, quit: ").strip().lower()
        if action == "add":
            task = input("Enter the task: ").strip()
            add_one_task(task)
        elif action == "delete":
            index = int(input("Enter the index of the task to delete: ").strip())
            delete_task(index)
        elif action == "save":
            save_todos(to_do_list)
        elif action == "quit":
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()