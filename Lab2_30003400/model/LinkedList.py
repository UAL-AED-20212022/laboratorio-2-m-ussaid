from model.Node import Node

class LinkedList:

    def __init__(self):

        self.start_node = None
    
    def traverse_list(self):

        if self.start_node is None:
            print("A lista não possui valores")
            return

        else:
            n =  self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.ref

    def insert_at_end(self, data):

        new_node = Node(data)

        if self.start_node is None:
            self.start_node = new_node
            return

        n = self.start_node

        while n.ref is not None:
            n = n.ref
        n.ref = new_node
    
    def insert_at_start(self, data):

        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    
    def insert_after_item(self, x, data):

        n = self.start_node
        print(n.ref)

        while n is not None:
            if n.item == x:
                break
            n = n.ref

        if n is None:
            print("O elemento não está na lista")

        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("A lista não possui valores")
            return
        
        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        n = self.start_node
        print(n.ref)

        while n.ref is not None:
            if n.ref.item is not None:
                if n.ref.item == x:
                    break 
                n = n.ref

        if n.ref is None:
            print("Elemento não encontrado na lista")

        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_at_index(self, index, data):

        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node

        i = 1
        n = self.start_node

        while i < index-1 and n is not None:
            n = n.ref
            i = i + 1

        if n is None:
            print("Índice não consta na lista")

        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            

    def get_count(self):

        if self.start_node is None:
            return 0

        n = self.start_node
        count = 0

        while n is not None:
            count += 1
            n = n.ref
        return count

    def search_item(self, x):

        if self.start_node is None:
            print("A lista não possui elementos")
            return

        n = self.start_node

        while n is not None:

            if n.item == x:
                print("Elemento encontrado")
                return True

            n = n.ref

        print("Elemento não encontrado")
        return False


    def delete_at_start(self):

        if self.start_node is None:
            print("A lista encontra-se vazia")
            return
        self.start_node = self.start_node.ref
    
    def delete_at_end(self):

        if self.start_node is None:
            print("A lista encontra-se vazia")
            return

        n = self.start_node

        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def delete_element_by_value(self, x):

        if self.start_node is None:
            print("A lista encontra-se vazia")
            return

        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return

        n = self.start_node

        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref

        if n.ref is None:
            print("Elemento não encontrado na lista")

        else:
            n.ref = n.ref.ref
            
    def reverse_linkedlist(self):

        prev = None
        n = self.start_node

        while n is not  None:
            next = n.ref
            n.ref = prev
            prev = n
            n = next

        self.start_node = prev
    
    def get_last_node(self): 

        n = 1
        temp = self.start_node
        length = 0
        
        while temp is not None:
            temp = temp.ref
            length += 1

        if n > length: 
            return

        temp = self.start_node

        for i in range(0, length - n):
            temp = temp.ref
        return temp.item