# Problem Name is &&& Search Tree &&& PLEASE DO NOT REMOVE THIS LINE. 
# Instructions to candidate.
# 1) Run this code in the REPL to observe its behaviour. The execution entry point is main().
# 2) Implement the "put" and "contains" methods.
# 3) Fix the "inOrderTraversal" method.
# 4) Add additional relevant tests
# 5) If time permits, try to improve your implementation. 
import unittest 
class BST(object):
    def __init__(self):
        self.root = Node()
    
    def put(self, value):
        self._put(value, self.root)

    def _put(self, value, node):
        if node.value is None:
            node.value = value
        else:
            if value < node.value:
                if node.left is None:
                    node.left = Node()
                self._put(value, node.left)
            else:
                if node.right is None:
                    node.right = Node()
                self._put(value, node.right)
    
    def contains(self, value):
        #TODO: implement me return False
        return self._contains(value, self.root)
    
    def _contains(self, value, node):
        if node is None or node.value is None:
            return False
        else:
            if value == node.value:
                return True
            elif value < node.value:
                return self._contains(value, node.left)
            else:
                return self._contains(value, node.right)

    def in_order_traversal(self):
        acc = list()
        self._in_order_traversal(self.root, acc)
        return acc

    def _in_order_traversal(self, node, acc):
        if node is None or node.value is None:
            return
        self._in_order_traversal(node.left, acc)
        acc.append(node.value)
        self._in_order_traversal(node.right, acc)

class Node(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
class TestBST(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.search_tree = BST()

    def test_bst(self):
        self.search_tree.put(3)
        self.search_tree.put(1)
        self.search_tree.put(2)
        self.search_tree.put(5)
        self.assertFalse(self.search_tree.contains(0))
        self.assertTrue(self.search_tree.contains(1))
        self.assertTrue(self.search_tree.contains(2))
        self.assertTrue(self.search_tree.contains(3))
        self.assertFalse(self.search_tree.contains(4))
        self.assertTrue(self.search_tree.contains(5))
        self.assertFalse(self.search_tree.contains(6))
        self.assertEqual(self.search_tree.in_order_traversal(), [1,2,3,5])
    
    #TODO: Write some more tests

    def test_empty(self):
        self.assertEqual(self.search_tree.in_order_traversal(), [])

    def test_negative(self):
        self.search_tree.put(-1)
        self.search_tree.put(11)
        self.search_tree.put(-10)
        self.search_tree.put(50)
        self.assertTrue(self.search_tree.contains(-1))
        self.assertTrue(self.search_tree.contains(11))
        self.assertTrue(self.search_tree.contains(-10))
        self.assertTrue(self.search_tree.contains(50))
        self.assertEqual(self.search_tree.in_order_traversal(), [-10,-1,11,50])

    def test_dupes(self):
        self.search_tree.put(1)
        self.search_tree.put(2)
        self.search_tree.put(1)
        self.search_tree.put(2)
        self.assertTrue(self.search_tree.contains(1))
        self.assertTrue(self.search_tree.contains(2))
        
        self.assertEqual(self.search_tree.in_order_traversal(), [1,1,2,2])

    def test_none(self):
        self.search_tree.put(None)
        self.assertFalse(self.search_tree.contains(None))
        self.assertEqual(self.search_tree.in_order_traversal(), [])

if __name__ == '__main__':
    unittest.main()