class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # To print the total LinkedList
    def print_LL(self):
        if self.head is None:
            print("The linkedlist is empty")
        else:
            tem = self.head
            while tem is not None:
                print(tem.data)
                tem = tem.next

    # Add at the beginning
    def add_begin(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    # add after the end Node
    def add_end(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            tem = self.head
            while tem.next is None:
                tem = tem.next
            new_node = Node(data)
            tem.next = new_node

    # Add after a given node
    def after_node(self, x, data):
        if self.head is None:
            print("Can not add as ll is empty")
        else:
            tem = self.head
            while tem.next is not None:
                if tem.data == x:
                    break
                tem = tem.next
            if tem.next is None:
                print(f"Enter data {x} is out of bound! ")
            else:
                new_node = Node(data)
                new_node.next = tem.next
                tem.next = new_node

    # add before a given node
    def before_node(self, x, data):
        if self.head is None:
            print("can not add as ll is empty")
        else:
            tem = self.head
            while tem.next is not None:
                if tem.next.data == x:
                    break
                tem = tem.next
            if tem.next is None:
                print(f"Enter data {x} is out of bound~!!")
            else:
                new_node = Node(data)
                new_node.next = tem.next
                tem.next = new_node

    # Delete by value of a node
    def delete_by_value(self, x):
        if self.head is None:
            print("Can not add as Ll is Empty")
        elif self.head.data == x:
            self.head = self.head.next
        else:
            tem = self.head
            while tem.next is not None:
                if tem.next.data == x:
                    break
                tem = tem.next
            if tem.next is None:
                print(f"Entered value {x} is Not found!!!")
            else:
                tem.next = tem.next.next

    # delete first node
    def delete_begining(self):
        if self.head is None:
            print("The LL is empty so can not be deleted!!!")
        else:
            self.head = self.head.next

    # delete the end node
    def delete_end(self):
        if self.head is None:
            print("The Ll is empty so can not be deleted!!")
        else:
            tem = self.head
            while tem.next.next is not None:
                tem = tem.next
            tem.next = None

    # delete next node of a given node
    def delete_next_node(self, x):
        if self.head is None:
            print("The Ll is empty so can not be deleted!!")
        else:
            tem = self.head
            while tem.next is not None:
                if tem.data == x:
                    break
                tem = tem.next
            if tem.next is None:
                print(f"The given value {x} is out of bound!!! ")
            else:
                tem.next = tem.next.next


LL = LinkedList()
LL.add_begin(40)
LL.add_begin(30)
LL.add_begin(20)
LL.add_begin(10)
LL.add_end(50)
LL.add_end(60)
LL.add_end(70)
LL.print_LL()
LL.after_node(400, 100)
LL.before_node(310, 5000)
LL.delete_by_value(10)
LL.delete_begining()
LL.delete_end()
LL.delete_next_node(330)


