# palindrome in singly linked-list

# Node class to crete a node
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# class linked_list to create a singly linked list
class linked_list:
    # constructor to initialize the head of the linked list
    def __init__(self):
        self.head = None

    # method to add a node to the linked list
    def add(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # method to reverse the linked list
    def reverse(self, val):
        node = None
        while val:
            tempt = val.next
            val.next = node
            node = val
            val = tempt

        return node

    # method to compare the linked list
    def compare(self, node1, node2):
        while node1 is not None and node2 is not None:
            if node1.data != node2.data:
                return False
            node1 = node1.next
            node2 = node2.next

        return True

    # method to check if the linked list is palindrome
    def palindrome(self):
        if self.head is None:
            return True

        node1 = self.head
        slow = node1
        fast = node1

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        node2 = self.reverse(slow.next)

        while node1 is not None and node2 is not None:
            if node1.data != node2.data:
                return False
            node1 = node1.next
            node2 = node2.next

        return True


# creating a singly linked list
single = linked_list()
single.add(1)
single.add(2)
single.add(3)
single.add(4)
# single.add(5)
single.add(2)
single.add(1)
print(single.palindrome())
