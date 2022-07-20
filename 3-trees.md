[Back to Welcome Page](0-welcome.md)

# Trees

![Family Tree](/Resources/family_tree.jpg)
^Image^ ^Credit:^ ^http://meandmyancestors.blogspot.com/p/my-family-tree.html^
If you have ever seen a family tree (the diagram showing relationships over generations in families), you are familiar with the concept of a tree. The idea is that each node is connected to no more than two additional nodes. It is similar to a linked list in that each node points to the next node(s).

The first node, at the top of the tree is called the root. Nodes that have sub-nodes are called parent nodes, with the connected nodes being child nodes. Nodes that do not connect to additional nodes are called leaves.
![Binary Tree](/Resources/binary_tree.jpeg)
^Image^ ^Credit:^ ^https://byui-cse.github.io/cse212-course/lesson09/09-prepare.html^

A <strong>Binary Search Tree</strong> (BST) is a binary tree that has rules implemented regarding the way data is added. These rules enable the searching of the tree to be very efficient - <strong>O(log n)</strong>. This is possible because each time you choose a direction to traverse, you are cutting the possible nodes to visit in half. The way that this works is that data is added based on its relationship with the root node. If the new value is less than the current node, you move to the left, if it's greater than, you move to the right. You repeat this process until you reach the end and can add a new node.

![BST](/Resources/bst.jpg)
For the example above, if we were going to add a node for the number 11, we would start at the root. Is 11 greater than or less than 20 (the value of the root node)? Less than, go to the next node on the left. Is 11 less than or greater than the value of the current node, which is 9? Greater than, go to the next node on the right. Is 11 less than or greater than the current node value of 18? Less than, go to the next node on the left - which is null, so we will add a new node to hold the value 11 to the left of the node containing 18.

You can see how this can simplify searching a tree. Let's say you are to find the number 11 (which we just added). You are going to follow the same logic, is the value I'm searching for greater or less than the root? If less than, go left. This automatically cuts down the amount of nodes we have to visit in half - assuming this is a balanced tree, which we will get to in a minute. At each intersection you make a choice and immediately cut down the number of nodes left to visit. In a balanced search tree, this gives you O(log n) efficiency. In an unbalanced tree, you could end up with O(n) efficiency.

A <strong>Balanced Binary Search Tree</strong> (balanced BST), is exactly as it sounds. It's maintaining a similar number of nodes on either side. The difference of height should be less than 2 to be considered balanced. To calculate the height, you start at the node immediately after the root and count the number of levels. In the example above, the far left (values 9 and 6) has a height of 2, so does the right branch of the left side of the tree (values 9 and 18). The right side has a height of 3. Since 3 minus 2 is 1, and 1 is less than 2, this is considered a balanced BST.

There are algorithms that can be used to detect when a tree becomes unbalanced and will then rework the tree to maintain balance. This is beyond the scope of this tutorial though, so we will not go into specifics on this.

Now that we have an idea of the layout of a tree, what can we do with it and how do we implement it? You will find that these operations are similar to those in linked lists. We implement a Node class and initiate a left pointer, right pointer, and the data variable (contains the value of the node). Once the tree is created, we can insert or remove a node or traverse the tree (visit each node).

Because Python does not have a built in class to handle Binary Search Trees, you either must build your own, or use an existing package. These classes typically contain similar functionality, as outlined below. Note that other than size() and empty(), these operations use recursion to complete its task.

| Operation         | Explanation                                                                                   | Performance |
| ----------------- | --------------------------------------------------------------------------------------------- | ----------- |
| insert(value)     | Insert the passed value into the tree                                                         | O(log n)    |
| remove(value)     | Remove the passed value from the tree                                                         | O(log n)    |
| contains(value)   | Returns whether value is found within the tree                                                | O(log n)    |
| traverse_forward  | Visits each node, starting at the left, then on the right                                     | O(n)        |
| traverse_backward | Visits each node, starting on the right, then on the left                                     | O(n)        |
| height(node)      | Calculates the height of a node - to get the height of the tree, pass in the root             | O(n)        |
| size()            | Returns the size of the tree. This info is kept within the class, making the performance O(1) | O(1)        |
| empty()           | Checks root node to see if empty - returns true if empty                                      | O(1)        |

### Real world use-cases

Binary Search Trees are used in rendering 3D games and a special type of BST, called a syntax tree, is used in building compilers.

## Code Example

For the code example we will demonstrate let's look at how to insert and forward traverse through the tree.

```
class BST:
    """
    Binary Search Tree data structure is implemented using the BST outer-class
    and an inner-class for the node
        """

    class Node:
        """
        Every node has a left, right, and data value accessible.
        """

        def __init__(self, data):
            """
            Sets the data value equal to the passed in value. Left and Right
            remain as None and are set as part of the insert process
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
        Using recursion, we will search the tree until we find a place for a new
        node and the data to be inserted. This function is called initially by
        the insert function.
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
        Uses recursion to traverse through the tree in order (forward).
        If the given node exists move to the left getting the smaller
        number first. After we yield the values from the left, we will
        yield the value of the current node, and then we will visit the
        right side and yield that value.

        (Left of cur_node, cur_node, right of cur_node (this provides
        the lowest value, middle value and then the larger value in
        ascending order.)

        This function should be called by
        the __iter__ function initially.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

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
```

## Try it for yourself

For the challenge, try traversing the tree backward and also try searching for to see if a value exists in the tree.

Find the solution [here](TreeDemo.py).

### Resources Used

^-^ ^https://byui-cse.github.io/cse212-course/lesson09/09-prepare.html^

^-^ ^https://www.tutorialspoint.com/python_data_structure/python_binary_search_tree.htm^

^-^ ^https://phuctm97.com/blog/binary-tree-seach-apps^
