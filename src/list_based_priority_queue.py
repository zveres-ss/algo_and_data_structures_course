class Node:
    def __init__(self, value=None, priority=None):
        self.value = value
        self.priority = priority
        self.next = None
        self.prev = None

class PriorityQueue:
    def __init__(self):
        self.head = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if not self.head:
            self.head = new_node
        elif priority > self.head.priority:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.priority >= priority:
                current = current.next
            if current.next:
                new_node.next = current.next
                current.next.prev = new_node
            current.next = new_node

            new_node.prev = current

    def remove_highest_priority(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return value

    def peek(self):
        if not self.head:
            return None
        return self.head.value

    def display(self):
        current = self.head
        while current:
            print(f"Завдання: {current.value}, Пріоритет: {current.priority}")
            current = current.next


if __name__ == "__main__":
    queue = PriorityQueue()
    while True:
        print("1. Додайте завдання")
        print("2. Видалити завдання з найвищим пріоритетом")
        print("3. Подивитись наступне завдання без видалення")
        print("4. Переглянути всі завдання")
        print("5. Вийти")
        choice = input("Введіть свій вибір: ")
        if choice == '1':
            task = input("Введіть завдання: ")
            priority = int(input("Введіть пріоритет: "))
            queue.insert(task, priority)
            print("Завдання додано до черги.")
        elif choice == '2':
            task = queue.remove_highest_priority()
            if task:
                print(f"Видалено завдання: {task}")
            else:
                print("Черга порожня.")
        elif choice == '3':
            task = queue.peek()
            if task:
                print(f"Наступне завдання без видалення: {task}")
            else:
                print("Черга порожня.")
        elif choice == '4':
            print("Всі завдання в черзі:")
            queue.display()
        elif choice == '5':
            print("Вихід..")
            break
        else:
            print("Невірний вибір. Будь ласка спробуйте ще раз.")
