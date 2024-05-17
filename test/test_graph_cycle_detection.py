from collections import deque
import unittest

def find_cycle(graph):
    n = len(graph)
    for start in range(n):
        visited = [False] * n
        queue = deque([(start, -1)])
        while queue:
            node, parent = queue.popleft()
            visited[node] = True
            for neighbor in range(n):
                if graph[node][neighbor]:
                    if neighbor != parent:
                        if visited[neighbor]:
                            return True
                        queue.append((neighbor, node))
    return False


def read_graph(filename):
    with open(filename, "r") as file:
        graph = []
        for line in file:
            graph.append(list(map(int, line.strip().split())))
    return graph


def write_result(filename, result):
    with open(filename, "w") as file:
        file.write(str(result))

class TestFindCycle(unittest.TestCase):
    def test_cycle(self):
        graph = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0]
        ]
        self.assertTrue(find_cycle(graph))

    def test_no_cycle(self):
        graph = [
            [0, 1, 0],
            [0, 0, 1],
            [0, 0, 0]
        ]
        self.assertFalse(find_cycle(graph))

if __name__ == "__main__":
    unittest.main()
