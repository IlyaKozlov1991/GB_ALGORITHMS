# Reverse doublelinked list

class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None

class doubleLinkedList:
    def __init__(self):
        self.start_node = None

    def insert(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("List is not empty")
    
    def insert_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            new_node = Node(data)
            new_node.next = self.start_node
            self.start_node.prev = new_node
            self.start_node = new_node

    def print_list(self):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.value, end=" ")
                n = n.next

    def reverse_list(self):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            start_value = self.start_node
            end_value = start_value.next
            start_value.next = None
            start_value.prev = end_value
            while end_value is not None:
                end_value.prev = end_value.next
                end_value.next = start_value
                start_value = end_value
                end_value = end_value.prev
            self.start_node = start_value

    def bubble_sort(self):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            sorted = False
            while not sorted:
                sorted = True
                n = self.start_node
                while n.next is not None:
                    if (n.value > n.next.value):
                        sorted = False
                        temp1 = n.value
                        n.value = n.next.value
                        n.next.value = temp1
                    n = n.next
                    
    

doublelist = doubleLinkedList()

doublelist.insert(1)
doublelist.insert_start(2)
doublelist.insert_start(3)
doublelist.insert_start(4)
doublelist.insert_start(5)
doublelist.insert_start(6)

doublelist.print_list()

# doublelist.bubble_sort()
doublelist.reverse_list()

print()
doublelist.print_list()