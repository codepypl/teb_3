from datetime import datetime


class Task:
    def __init__(self, name, description, priority, active_due):
        self.name = name
        self.description = description
        self.priority = priority
        self.created_at = datetime.now()
        self.active_due = datetime.strptime(active_due, "%Y-%m-%d")
        self.completed = False

    def mark_as_completed(self):
        self.completed = True


class TaskMngr:
    def __init__(self):
        self.tasks = []

    def mark_task_as_completed(self, task_id):
        if 0 <= task_id <= len(self.tasks):
            self.tasks[task_id].mark_as_completed()
            print(f"Zadanie o id {task_id} zostało oznaczone jako zakończone")
        else:
            print("Nieprawoidłowe id zadania")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Zadanie {task.name} zostało dodane.")

    def remove_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            removed_task = self.tasks.pop(task_id)
            print(f"Zadanie: {removed_task.name} zostało usunięt")
        else:
            print(f"Nieprawidłowe id {task_id}")

    def view_tasks(self):
        if not self.tasks:
            print("Brak zadań w systemie")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i}: {task.name}")


def menu():
        print("Co chcesz zrobić ? ")
        print(f"1. Dodaj nowe zadanie")
        print(f"2. Usuń zadanie")
        print(f"3. Oznacz zadanie jako wykonane")
        print("4. Pokaż listę zadań")


def main():
    task_manager = TaskMngr()
    while True:
        menu()
        choice = input("Wybierz czynność: ")
        if choice == "1":
            name = input(f"Nazwa zadania: ")
            description = input("Opis: ")
            priority = input(f"Priorytet zadania 1 - niski, 5 - wysoki: ")
            due_date = input(f"Termin wykonania zadania (YYYY-MM-RR): ")
            task_manager.add_task(Task(name, description, priority, due_date))
        elif choice == "2":
            task_id = int(input("Podaj nr zadania do usunięcia: "))
            task_manager.remove_task(task_id=task_id)
        elif choice == "3":
            task_id = int(input("Podaj nr zadania aby oznaczyć je jako gotowe: "))
            task_manager.mark_task_as_completed(task_id=task_id)
        elif choice == "4":
            print("Lista zadań: ")
            task_manager.view_tasks()
        else:
            print("Nieprawidłowa akcja")


if __name__ == "__main__":
    main()

