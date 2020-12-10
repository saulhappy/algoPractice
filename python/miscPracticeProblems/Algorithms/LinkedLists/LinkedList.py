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
        print(f"{current_node.next.data} added to the linked list")
    
    def length(self):
        current_node = self.head
        node_count = 0

        while current_node.next != None:
            node_count += 1
            current_node = current_node.next
        return node_count
    
    def get_at(self, index):
        if index >= self.length() or index < 0:
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
        list_data = "The linked list is: "
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next
            list_data += str(current_node.data) + "->"
        return list_data

    def delete_at(self, index):
        if index > self.length() or index < 0:
            print("ERROR: Index out of bounds")
            return None
        
        counter = 0
        current_node = self.head

        while current_node.next != None:
            previous_node = current_node
            current_node = current_node.next
            if counter == index:
                previous_node.next = current_node.next
                print(f"{previous_node.data} deleted from the linked list")
                return
            counter += 1

    def removeElements(self, val):
        """ explantion: https://www.youtube.com/watch?v=MFrwAUAv2hA"""
        
        dummy_node = node(None)
        dummy_node.next = self.head
        previous_node = dummy_node
        current_node = previous_node.next

        while(current_node):
            if current_node.data == val:
                previous_node.next = current_node.next
            else:
                previous_node = previous_node.next
            current_node = current_node.next
        return dummy_node.next



l = linked_list()

l.append(4)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(4)
l.append(4)


# print(l.length())
# print(l.print_list())
# l.delete_at(3)

print(l.print_list())
l.removeElements(4)
print(l.print_list())


