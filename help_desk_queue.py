# help_desk_queue.py
"""
Help desk ticketing system using a custom Queue built from Node (node.py).

Provides a small CLI:
1. Add customer
2. Help next customer
3. View next customer
4. View all waiting customers
5. Exit
"""

from node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            # empty queue
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if not self.front:
            return None
        node = self.front
        self.front = node.next
        if self.front is None:
            # queue became empty
            self.rear = None
        node.next = None
        return node.value

    def peek(self):
        return self.front.value if self.front else None

    def print_queue(self):
        if not self.front:
            print("(empty)")
            return
        current = self.front
        while current:
            print(f"- {current.value}")
            current = current.next


def help_desk_cli():
    queue = Queue()

    menu = """--- Help Desk Ticketing System ---
1. Add customer
2. Help next customer
3. View next customer
4. View all waiting customers
5. Exit
Select an option: """

    while True:
        try:
            choice = input(menu).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if choice == "1":
            name = input("Enter customer name: ").strip()
            if name == "":
                print("Customer name cannot be empty.\n")
                continue
            queue.enqueue(name)
            print(f"{name} added to the queue.\n")

        elif choice == "2":
            helped = queue.dequeue()
            if helped is None:
                print("No customers to help.\n")
            else:
                print(f"Helped: {helped}\n")

        elif choice == "3":
            nxt = queue.peek()
            if nxt is None:
                print("Next customer: (none)\n")
            else:
                print(f"Next customer: {nxt}\n")

        elif choice == "4":
            print("Waiting customers:")
            queue.print_queue()
            print()

        elif choice == "5":
            print("Exiting.")
            break

        else:
            print("Invalid option. Please choose 1-5.\n")


if __name__ == "__main__":
    help_desk_cli()

