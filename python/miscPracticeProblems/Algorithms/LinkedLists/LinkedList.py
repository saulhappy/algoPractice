# Definition for singly-linked list.
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
    
    def length(self):
        current_node = self.head
        node_count = 0

        while current_node.next != None:
            node_count += 1
            current_node = current_node.next
        return node_count



a = node("a")
b = node("b")
c = node("c")

l = linked_list()
l.append(a)
l.append(b)
l.append(c)

print(l.length())
