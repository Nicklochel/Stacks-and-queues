# undo_redo_system.py
"""
Undo/Redo system using a custom Stack built from Node (node.py).

Provides a small CLI:
1. Perform action
2. Undo
3. Redo
4. View Undo Stack
5. View Redo Stack
6. Exit
"""

from node import Node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            return None
        node = self.top
        self.top = node.next
        node.next = None
        return node.value

    def peek(self):
        return self.top.value if self.top else None

    def print_stack(self):
        print_stack_items = []
        current = self.top
        while current:
            print_stack_items.append(current.value)
            current = current.next
        if not print_stack_items:
            print("(empty)")
            return
        for item in print_stack_items:
            print(f"- {item}")

    def clear(self):
        self.top = None


def undo_redo_cli():
    undo_stack = Stack()
    redo_stack = Stack()

    menu = """--- Undo/Redo Manager ---
1. Perform action
2. Undo
3. Redo
4. View Undo Stack
5. View Redo Stack
6. Exit
Select an option: """

    while True:
        try:
            choice = input(menu).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ").rstrip("\n")
            undo_stack.push(action)
            # clear redo stack because new action path diverges
            redo_stack = Stack()
            print(f"Action performed: {action}\n")

        elif choice == "2":
            val = undo_stack.pop()
            if val is None:
                print("No actions to undo\n")
            else:
                redo_stack.push(val)
                print(f"Undid action: {val}\n")

        elif choice == "3":
            val = redo_stack.pop()
            if val is None:
                print("No actions to redo\n")
            else:
                undo_stack.push(val)
                print(f"Redid action: {val}\n")

        elif choice == "4":
            print("Undo Stack:")
            undo_stack.print_stack()
            print()

        elif choice == "5":
            print("Redo Stack:")
            redo_stack.print_stack()
            print()

        elif choice == "6":
            print("Exiting.")
            break

        else:
            print("Invalid option. Please choose 1-6.\n")


if __name__ == "__main__":
    undo_redo_cli()
