import unittest
from src.list_based_priority_queue import PriorityQueue

class TestPriorityQueueMethods(unittest.TestCase):
    def test_insert_and_peek(self):
        queue = PriorityQueue()
        queue.insert("Task 1", 3)
        queue.insert("Task 2", 5)
        queue.insert("Task 3", 2)
        self.assertEqual(queue.peek(), "Task 2")

    def test_remove_highest_priority(self):
        queue = PriorityQueue()
        queue.insert("Task 1", 3)
        queue.insert("Task 2", 5)
        queue.insert("Task 3", 2)
        removed_task = queue.remove_highest_priority()
        self.assertEqual(removed_task, "Task 2")
        self.assertEqual(queue.peek(), "Task 1")

    def test_display(self):
        queue = PriorityQueue()
        queue.insert("Task 1", 3)
        queue.insert("Task 2", 5)
        queue.insert("Task 3", 2)
        expected_output = "Завдання: Task 2, Пріоритет: 5\nЗавдання: Task 1, Пріоритет: 3\nЗавдання: Task 3, Пріоритет: 2\n"
        import io
        from contextlib import redirect_stdout
        with io.StringIO() as buf, redirect_stdout(buf):
            queue.display()
            self.assertEqual(buf.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
