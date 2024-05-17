from src.telecommunication_network import DisjointSet, kruskal
import unittest

class TestDisjointSet(unittest.TestCase):
    def test_disjoint_set(self):
        ds = DisjointSet(5)
        self.assertEqual(ds.find(0), 0)
        self.assertEqual(ds.find(1), 1)
        self.assertEqual(ds.find(2), 2)
        self.assertEqual(ds.find(3), 3)
        self.assertEqual(ds.find(4), 4)

        ds.union(0, 1)
        ds.union(2, 3)
        ds.union(1, 4)

        self.assertEqual(ds.find(0), ds.find(1))
        self.assertEqual(ds.find(1), ds.find(4))
        self.assertEqual(ds.find(2), ds.find(3))
        self.assertNotEqual(ds.find(0), ds.find(2))
        self.assertNotEqual(ds.find(0), ds.find(3))

class TestKruskal(unittest.TestCase):
    def test_kruskal(self):
        graph1 = [(0, 1, 5), (0, 2, 10), (1, 2, 20)]
        graph2 = [(0, 1, 10), (0, 2, 15), (1, 2, 5)]
        graph3 = [(0, 1, 100), (1, 2, 50), (0, 2, 200)]

        self.assertEqual(kruskal(graph1), 15)
        self.assertEqual(kruskal(graph2), 15)
        self.assertEqual(kruskal(graph3), 150)

if __name__ == '__main__':
    unittest.main()

