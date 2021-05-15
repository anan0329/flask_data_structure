class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        """docstring for __init__"""
        self.head = None
        self.last_node = None
        
    def to_list(self):
        l = []
        if self.head is None:
            return l
        
        node = self.head
        while node:
            l.append(node.data)
            node = node.next_node
        return l
    
    def print_ll(self):
        """
        ll = LinkedList()
        node4 = Node("data4", None)
        node3 = Node("data3", node4)
        node2 = Node("data2", node3)
        node1 = Node("data1", node2)
        
        ll.head = node1
        ll.print_ll()
        
        result: data1 -> data2 -> data3 -> data4 -> None
        """
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node
            
        ll_string += " None"
        print(ll_string)
        
    def insert_beginning(self, data):
        """
        ll = LinkedList()
        ll.insert_beginning("data")
        ll.insert_beginning("data new")
        ll.print_ll()
        
        result: data new -> data -> None
        """
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
        
        new_node = Node(data, self.head)
        self.head = new_node
        
    def insert_at_end(self, data):
        """
        ll = LinkedList()
        ll.insert_beginning("data")
        ll.insert_beginning("data")
        ll.insert_beginning("data")
        ll.insert_at_end("end")
        ll.insert_at_end("end2")
        ll.print_ll()
        """
        if self.head is None:
            self.insert_beginning(data)
        
        # if self.last_node is None:
        #     node = self.head
        #     # get the last node
        #     while node.next_node:
        #         node = node.next_node
        #     
        #     node.next_node = Node(data, None)
        #     self.last_node = node.next_node
        # else:
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node
    
    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            # node.data["id"] because the data is a dicrionary form
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next_node
        return None


# ll = LinkedList()
# # head last_node: None
# ll.insert_beginning("data")
# # new_node :: data:"data" next_node:None
# # head:"data" next_node:None
# ll.insert_beginning("data new")
# # new_node :: data:"data new" next_node:"data"
# # head:"data new" next_node:"data"
# ll.print_ll()
# ll = LinkedList()
# ll.insert_beginning("data")
# ll.insert_beginning("data")
# ll.insert_beginning("data")
# ll.insert_at_end("end")
# ll.insert_at_end("end2")
# ll.print_ll()
