class BST:
    """
    Binary Search Tree data structure is implemented using the BST outer-class and an inner-class for the node
        """

    class Node:
        """
        Every node has a left, right, and data value accessible.  
        """

        def __init__(self, data):
            """ 
            Sets the data value equal to the passed in value. Left and Right remain as None and are set as part of the insert process
            """

            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert data into the tree. If the BST
        is empty, we'll set the root equal to the new 
        node.  If it's not empty, call _insert to recursively
        search for a place to insert the data.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        """
        Using recursion, we will search the tree until we find a place for a new node and the data to be inserted.
        This function is called initially by the insert function
        """
        if data == node.data:
            err = 'Item already exists. No duplicates allowed.'
            return err
        elif data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)

    def __iter__(self):
        """
        Iterate through the tree, beginning at the root. This function should be
        used within a loop:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root

    def _traverse_forward(self, node):
        """
        Uses recursion to traverse through the tree in order (forward). If the given node exists move
        to the left getting the smaller number first. After we yield the values from the left, we 
        will yield the value of the current node, and then we will visit the right side and yield that value.

        (Left of cur_node.data, cur_node.data, right of cur_node.data (this provides lowest value, middle value 
        and the larger value in ascending order.)

        This function should be called by 
        the __iter__ function initially.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
#####################
# REVERSE TRAVERSAL #
#####################

    def __reversed__(self):
        """
        Iterate through the tree backward - begin at the root. This function should be
        used within a loop:

        for value in reversed(my_bst):
            print(value)

        """
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node):
        """
        Uses recursion to return the values highest to lowest (reverse order). If the given node exists move 
        to the right, getting largest number first. After that value is returned, yield the value of the current
        node and then the value from the node to the right.

        This function should be called initially by 
        the __reversed__ function.        
        """
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

    #################
    # VALUE EXISTS? #
    #################

    def __contains__(self, data):
        """ 
        Checks to see if data exists in the tree.  The keyword
        'in' may be used with this function:

        if 6 in my_tree:
            ("6 is in the tree")

        """
        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
        """
        Search for an existing value within the tree. This function
        should be called initially by the __contains__ function.
        """
        # if the tree is empty: FALSE
        if self.root == None:
            return False

        # if the value is found on the current node: TRUE
        if data == node.data:
            return True

        # if the value is less than the value on current node, recursively call this function passing the node to the left
        elif data < node.data:
            if node.left:
                return self._contains(data, node.left)

        # if the value is greater than the value on current node, recursively call this function passing the node to the right
        elif data > node.data:
            if node.right:
                return self._contains(data, node.right)


# --------------------------------------------------------
# ---------------------- TEST CASES ----------------------
# --------------------------------------------------------
tree = BST()
tree.insert(45)
tree.insert(22)
tree.insert(13)
tree.insert(99)
tree.insert(68)
tree.insert(49)
tree.insert(30)
tree.insert(26)
tree.insert(42)

print(f"root: {tree.root.data}")  # expected: 45

for n in tree:
    print(n)  # expected: 13, 22, 26, 30, 42, 45, 49, 68, 99
