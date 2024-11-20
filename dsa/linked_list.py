class node:
    def __init__(self, data):
        self.data = data
        self.next = None


# singly linked list
class linked_list:
    def __init__(self):
        self.head = None

    def add(self, val):
        new_node = node(val)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, key):
        current = self.head

        # if key is found, get the previous node
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # if key is not found
        if current is None:
            print("key not found")
            return

        # if key is found
        prev.next = current.next
        current = None

    # insert at any position
    def insert(self, pos, val):
        new_node = node(val)
        current = self.head

        for _ in range(pos - 1):
            current = current.next

        if current is None:
            print("Position not found")
            return

        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end="=>")
            current = current.next
        print()


singly = linked_list()
singly.add(1)
singly.add(2)
singly.add(3)
# singly.display()
# singly.remove(2)
singly.insert(1, 4)
singly.insert(5, 5)
singly.display()

# when you check the current value, then you have to update to the next value