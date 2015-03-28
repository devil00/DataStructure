import unittest
import random
from binary_search_tree import BinarySearchTree 


def is_bst(root, min_data, max_data):
    if root is None:
        return True
    if root.data <= min_data or root.data >= max_data:
        return False
    status = is_bst(root.left, min_data, root.data)
    status = status and is_bst(root.right, root.data, max_data)

    return status
        

class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        self.nodes_data1 = [9, 4, 2, 2, 1, 3, 6, 5]
        self.nodes_data2 = [7, 14, 5, 10, 20, 6, 11, 13, 45, 15, 16]

    def test_insert(self):
        for nd in self.nodes_data2:
            self.bst.insert(nd)
        self.assertTrue(
            is_bst(self.bst.root, float('-infinity'), float('infinity')))

        self.bst = BinarySearchTree()

        for nd in self.nodes_data1:
            self.bst.insert(nd)
        self.assertFalse(is_bst(
            self.bst.root, float('-infinity'), float('infinity')))

    def test_traversals(self):
        for nd in self.nodes_data2:
            self.bst.insert(nd)
        traversed_nodes = self.bst.inorder()
        self.assertEquals(traversed_nodes, sorted(self.nodes_data2))
        traversed_nodes = self.bst.preorder()
        self.assertEquals(traversed_nodes,
                          [7, 5, 6, 14, 10, 11, 13, 20, 15, 16, 45])
        traversed_nodes = self.bst.postorder()
        self.assertEquals(traversed_nodes,
                          [6, 5, 13, 11, 10, 16, 15, 45, 20, 14, 7])

    def test_delete(self):
        for nd in self.nodes_data2:
            self.bst.insert(nd)

        # node is not present in a bst
        self.assertIsInstance(self.bst.delete(1000), str)

        # delete node with single child 5
        self.bst.delete(5)
        traversed_nodes = self.bst.postorder()
        self.assertEquals(
            traversed_nodes, [6, 13, 11, 10, 16, 15, 45, 20, 14, 7])
        
        # delete node with two child 14
        self.bst.delete(14)
        traversed_nodes = self.bst.postorder()
        self.assertEquals(
            traversed_nodes, [6, 13, 11, 10, 16, 15, 45, 20, 7])
        traversed_nodes = self.bst.inorder()
        self.assertEquals(traversed_nodes, [6, 7, 10, 11, 13, 15, 16, 20, 45])

        # delete node with no child 45
        self.bst.delete(45)
        traversed_nodes = self.bst.postorder()
        self.assertEquals(
            traversed_nodes, [6, 13, 11, 10, 16, 15, 20, 7])

    def test_search(self):
        for nd in self.nodes_data2:
            self.bst.insert(nd)

        self.assertTrue(self.bst.search(15))
        self.assertFalse(self.bst.search(100))

    def test_count_nodes(self):
        for nd in self.nodes_data2:
            self.bst.insert(nd)

        self.assertEquals(self.bst.count_nodes(), 11)

    def tearDown(self):
        self.bst = None

if __name__ == "__main__":
    unittest.main()
