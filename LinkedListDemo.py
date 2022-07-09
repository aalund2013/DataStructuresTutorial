class LinkedList:
    """
    LinkedList data structure is implemented using the 
    LinkedList outer-class and an inner-class for the node
    """

    class Node:
        """
        Every node will have a next, prev, and data value that can be accessed
        """

        def __init__(self, data):
            """ 
            Sets the default values for the node upon creation
            """
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.tail = None

    def insert_into(self, existing_value, new_value):
        """
        Insert a new node after the first node containing a specified value
        """
        cur_node = self.head
        while cur_node is not None:

            if cur_node.data == existing_value:  # check to see if node matches existing_value

                if cur_node == self.tail:
                    # re-use the function for inserting at the tail
                    insert_tail(new_value)

                else:
                    new_node = LinkedList.Node(new_value)  # create new_node
                    new_node.prev = cur_node  # set the prev value on the new_node
                    new_node.next = cur_node.next  # set the next value on the new_node
                    cur_node.next.prev = new_node  # update the prev value to point to new_node
                    cur_node.next = new_node  # update the next value of cur_node to point to new_node

                return

            cur_node = cur_node.next

    def insert_tail(self, value):
        """
        Insert a new node at the back of the Linked List
        """
        new_node = LinkedList.Node(value)

        if self.head is None:  # if list is empty, create node and set as head and tail
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail  # set pointer on new_node to the previous tail
            self.tail.next = new_node  # set pointer on previous tail to new_node
            self.tail = new_node  # set tail to point to new_node

    def traverse_ll(self):
        cur_node = self.head  # set current node to head
        while cur_node is not None:
            yield cur_node.data  # return the value
            cur_node = cur_node.next  # set current node to next node

    def find_remove(self, value):
        cur_node = self.head  # begin traversing the list
        while cur_node is not None:
            if cur_node.data == value:  # check to see if values match
                if cur_node == self.head:
                    cur_node.next.prev = None  # remove the prev pointer on the next node
                    cur_node.next = self.head  # set the next node to the head
                if cur_node == self.tail:
                    cur_node.prev.next = None  # remove the next pointer on the previous node
                    cur_node.prev = self.tail  # set the previous node to the tail
                else:
                    # change node to the left's next value to point to node to right of cur_node
                    cur_node.prev.next = cur_node.next
                    # change node to the right's prev value to point to node to left of cur_node
                    cur_node.next.prev = cur_node.prev
            cur_node = cur_node.next


lnkList = LinkedList()
lnkList.insert_tail("Harry Potter and the Sorcerer's Stone")
lnkList.insert_tail("Harry Potter and the Philosopher's Stone")
lnkList.insert_tail("Chamber of Secrets")
lnkList.insert_tail("Goblet of Fire")
lnkList.insert_tail("Order of the Phoenix")
lnkList.insert_tail("Half-Blood Prince")
lnkList.insert_tail("Sirius James Potter and the Dark Secret")
# Output: ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Philosopher's Stone", 'Chamber of Secrets', 'Goblet of Fire', 'Order of the Phoenix', 'Half-Blood Prince', 'Sirius James Potter and the Dark Secret']
print(list(lnkList.traverse_ll()))

# add the 3rd and 7th Harry Potter books into it's proper place in the linked list
# insert Prisoner of Azkaban AFTER Chamber of Secrets
lnkList.insert_into("Chamber of Secrets", "Prisoner of Azkaban")
# insert Deathly Hallows AFTER Half-Blood Prince
lnkList.insert_into("Half-Blood Prince", "Deathly Hallows")
# Output: ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Philosopher's Stone", 'Chamber of Secrets', 'Prisoner of Azkaban', 'Goblet of Fire', 'Order of the Phoenix', 'Half-Blood Prince', 'Deathly Hallows', 'Sirius James Potter and the Dark Secret']
print(list(lnkList.traverse_ll()))

lnkList.find_remove("Harry Potter and the Philosopher's Stone")
lnkList.find_remove("Sirius James Potter and the Dark Secret")
lnkList.find_remove("Non-Existence")
# Output: ["Harry Potter and the Sorcerer's Stone", 'Chamber of Secrets', 'Prisoner of Azkaban', 'Goblet of Fire', 'Order of the Phoenix', 'Half-Blood Prince', 'Deathly Hallows']
print(list(lnkList.traverse_ll()))
