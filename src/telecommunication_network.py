class DisjointSet:
    """Клас для представлення набору неперетинаючих множин."""

    def __init__(self, elements):
        """
        Ініціалізує новий об'єкт DisjointSet з n елементами.
        :param elements: Кількість елементів.
        """
        self.parent = [i for i in range(elements)]
        self.rank = [0] * elements

    def find(self, element):
        """
        Повертає представника множини, до якої належить елемент.

        :param element: Елемент.
        :return: Представник множини.
        """
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, element1, element2):
        """
        Об'єднує дві множини, в яких знаходяться вказані елементи.

        :param element1: Перший елемент.
        :param element2: Другий елемент.
        :return: True, якщо об'єднання відбулося, False - в іншому випадку.
        """
        parent1, parent2 = self.find(element1), self.find(element2)
        if parent1 == parent2:
            return False
        if self.rank[parent1] < self.rank[parent2]:
            self.parent[parent1] = parent2
        elif self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
        else:
            self.parent[parent2] = parent1
            self.rank[parent1] += 1
        return True

def kruskal(graph):
    """
    Знаходить мінімальне кісткове дерево в графі за допомогою алгоритму Крускала.

    :param graph: Список ребер графа у вигляді (вузол1, вузол2, вага).
    :return: Мінімальна вага кісткового дерева.
    """
    graph.sort(key=lambda x: x[2])
    elements_count = len(graph)    #можна ці дві строки замінити на просто ds=DisjointSet(len(graph))
    ds = DisjointSet(elements_count)
    min_cost = 0
    for element1, element2, weight in graph:
        if ds.union(element1 - 1, element2 - 1):   #не потрібно віднімати -1 оскільки індекси вже адаптовані у джоінсеті
            min_cost += weight
    return min_cost


def main():
    """
    Основна функція програми.
    Зчитує дані з файлу 'communication_wells.csv' та знаходить мінімальну довжину оптоволоконного кабелю.
    """
    graph = []
    with open('communication_wells.csv', 'r') as file:
        for line in file:
            node1, node2, distance = line.strip().split(',')
            graph.append((int(node1) - 1, int(node2) - 1, int(distance)))

    min_cable_length = kruskal(graph)

    if min_cable_length == 0:
        print("Колодязі не зв'язані між собою.")
    else:
        print(f"Мінімальна довжина оптоволоконного кабелю: {min_cable_length}")

if __name__ == "__main__":
    main()
