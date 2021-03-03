"""
Kai Matkin

This is a SOLUTION. Review over this code only after you have tried to
solve the problems on your own. 
"""

"""
This class sets up the BST. It has a set of functions and a Node class to 
implement some the tree.
"""
class BST:

    """
    This class creates nodes on the BST. Since it is an inner class, the 
    only way to access it is through the BST class.
    """
    class Node:
        
        """
        In order to create a tree there needs to be links to the left and
        the right for the node to connect to. This part initializes them
        but until they are populated with data it is set to none.
        """
        def __init__(self, data):
       
            self.data = data
            self.left = None
            self.right = None
    
    """
    Similar to the node init function this will initialize the BST, but
    since nothing has been given to populated the data yet the root is
    set to none.
    """
    def __init__(self):
        self.root = None

    """
    This will initialize the process for adding data to the node in the
    tree. First the insert function checks if the root has been populated
    yet. If it is not then the data is added as the root. Otherwise the 
    _insert function will be called to add in the data to a node.
    """
    def insert(self, data):
        #Checks that the root is already populated
        if self.root is None:
            self.root = BST.Node(data)
        #Then calls the _add_in function
        else:
            self._add_in(data, self.root)

    """
    Using recursion this will properly store the data into the correct 
    node. For BSTs nodes on the right are larger than the current node. 
    Nodes on the left are smaller than the current node. No duplicate 
    values will be accepted and placed into the tree.
    """
    def _add_in(self, data, node):
        # Problem #1
        #If the data is greater than what is in the node, look on the right
        if data > node.data:
            #If there is no data in the node, we found an empty one we can populate
            if node.right is None:
                node.right = BST.Node(data)
            #If there is data in the node continue looking in the tree.
            else:
                self._add_in(data, node.right)
        elif data < node.data:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._add_in(data, node.left)
        #Notice there are no equals to signs in this function. 
        #There should not be any duplicate data allowed.

    """
    This will work to iterate forwards through the tree. It starts with
    the root and then calls another function so that recursion can be
    used to loop through the rest of the tree. 
    """
    def __iter__(self):
        yield from self._traversing_forwards(self.root)
        
    """
    After having been called in the iterate function _traversing_forwards
    will be used recursively. It should yield at each node so that a loop
    can be performed with the data from each node. It should traverse 
    through from the smallest to the largest items stored in the tree.
    """
    def _traversing_forwards(self, node):
        # Problem #2
        #Same concept as iterating backwards, but in reversed order.
        if node is not None:
            yield from self._traversing_forwards(node.left)
            yield node.data
            yield from self._traversing_forwards(node.right)
    
    """
    This is the same code that we worked through together. This function
    will be used to traverse backwards through the tree. 
    """
    def __reversed__(self):    
        yield from self._traversing_backwards(self.root)

    """
    The is the second function we worked through together. It uses 
    recursion to start at the largest node first (farthest to the right) 
    and then ends at the smallest node (farthest to the left).
    """
    def _traversing_backwards(self, node):
        if node is not None:
            yield from self._traversing_backwards(node.right)
            yield node.data
            yield from self._traversing_backwards(node.left)

medtree = BST()
medtree.insert(8)
medtree.insert(12)
medtree.insert(14)
medtree.insert(4)  
medtree.insert(10)
medtree.insert(6)
medtree.insert(7)
medtree.insert(2)
medtree.insert(7)
print("Traversing Forwards:")
for i in medtree:
    print(i)  # 2, 4, 6, 7, 8, 10, 12, 14

"""Sample code to show that the traversing backwards function works"""
print("\nTraversing Backwards:")
for i in reversed(medtree):
    print(i)  # 14, 12, 10, 8, ,7, 6, 4, 2