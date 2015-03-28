'''
This module implements the Binary Search Tree with the following methods:
    insert
    delete
    search
    inorder
    preorder
    postorder

@author: Mayur Swami
@date: March 27, 2015
'''


class BSTNode(object):
    '''
    This represents the node of Binary Search Tree. It also contains 2 
    child nodes or subnodes and the data variable.
    '''
    def __init__(self, data=0):
        self._data = data
        self._left = None
        self._right = None

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value


class BinarySearchTree(object):
    '''
    Implementation of BST such that every left node is lesser than the main 
    node and every right is greater than the main node.
    '''
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        '''
        Add a node to a BST.
        :param node: a node to be added.
        :type node: instance of `~BSTNode`
        '''
        if node is None:
            node = BSTNode(data)
        else:
            if data <= node.data:
                node.left = self._insert(node.left, data)
            else:
                node.right = self._insert(node.right, data)
        return node

    def delete(self, data):
        if self.is_empty():
            print 'Tree is empty'
        elif not self.search(data):
            return '{} is not present in the tree'.format(data)
        else:
            self.root = self._delete(self.root, data)
            print '{} deleted from the tree'.format(data)

    def _delete(self, root, data):
        '''
        Delete a node from BST.
        :param root: Root node of BST.
        :type root: Instance of `~BST`
        :param data: content for which node must be deleted.
        :type data: Any datatype. Optional default to int.
        '''
        if root.data == data:
            lt = root.left
            rt = root.right
            if lt is None and rt is None:
                return None
            elif lt is None:
                return rt
            elif rt is None:
                return lt
            else:
                # Replace node to be deleted N with it's inorder successor 
                # with least value in it's right subtree.
                p1 = rt
                p2 = rt
                while p1.left is not None:
                    p1 = p1.left
                p1.left = lt
                return p2
        else:
            if data < root.data:
                root.left = self._delete(root.left, data)
            else:
                root.right = self._delete(root.right, data)

        return root

    def count_nodes(self):
        '''
        Returns the count of total number of nodes available in a BST.
        '''
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        if node is None:
            return 0
        else:
            l = 1
            l += self._count_nodes(node.left)
            l += self._count_nodes(node.right)
            return l

    def search(self, data):
        '''
        Search a specific content in a BST.
        :returns: True if element found or else False.
        '''
        return self._search(self.root, data)

    def _search(self, node, data):
        found = False
        while node is not None and not found:
            val = node.data
            if data < val:
                node = node.left
            elif data > val:
                node = node.right
            else:
                found = True
                break
            found = self._search(node, data)
        return found

    def inorder(self):
        traversal_nodes = []
        self._inorder(self.root, traversal_nodes)
        return traversal_nodes

    def _inorder(self, root, traversal_nodes):
        if root is not None:
            self._inorder(root.left, traversal_nodes)
            # sys.stdout.write('{} '.format(root.data))
            traversal_nodes.append(root.data)
            self._inorder(root.right, traversal_nodes)

    def preorder(self):
        traversal_nodes = []
        self._preorder(self.root, traversal_nodes)
        return traversal_nodes

    def _preorder(self, root, traversal_nodes):
        if root is not None:
            traversal_nodes.append(root.data)
            self._preorder(root.left, traversal_nodes)
            self._preorder(root.right, traversal_nodes)

    def postorder(self):
        traversal_nodes = []
        self._postorder(self.root, traversal_nodes)
        return traversal_nodes

    def _postorder(self, root, traversal_nodes):
        if root is not None:
            self._postorder(root.left, traversal_nodes)
            self._postorder(root.right, traversal_nodes)
            # sys.stdout.write('{} '.format(root.data))
            traversal_nodes.append(root.data)
    

if __name__ == "__main__":
    nodes = [7, 14, 5, 10, 20, 6, 11, 13, 45, 15, 16]
    tree = BinarySearchTree()
    for n in nodes:
        tree.insert(n)
    print tree.postorder()
    print "\n"
    print tree.preorder()
    print "\n"
    print tree.inorder()
    print "\n"
    print tree.count_nodes()
    print tree.search(10)
    tree.delete(14)
    print tree.postorder()
    tree.delete(5)
    print tree.postorder()
    
