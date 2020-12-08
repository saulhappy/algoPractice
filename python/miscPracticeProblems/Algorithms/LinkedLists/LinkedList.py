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
    
    def get_at(self, index):
        if index >= self.length():
            print("ERROR: Index out of bounds")
            return None
        
        counter = 0
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next
            if index == counter:
                return current_node.data
            else:
                counter += 1


    def print_list(self):
        list_data = ""
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next
            list_data += str(current_node.data) + "->"
        return list_data



l = linked_list()

l.append(1)
l.append(2)
l.append(3)

print(l.length())
print(l.print_list())
print(l.get_at(5))
