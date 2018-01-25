# -*- coding: utf-8 -*-
from node import Node

class LinkedList:     
    def __init__(self, value, pointer):
        self.head = Node(value, pointer)
        self.length = 1  
    
    def __len__(self):
        return self.length
    
    def __getitem__(self, pos):
        if (pos > self.length) or (pos < 1):
            raise ValueError("position is not suitable")
        counter = 1
        tmp = self.head
        while counter != pos:
            tmp = tmp.get_pointer()
            counter += 1
        return tmp            
    
    def insert(self, value, pos):        
        if self.length < pos or pos < 1:
            raise ValueError("pos is greater than the length")
        if pos == 1:
            tmp = self.head
            self.head = Node(value, tmp)
            
        elif pos == self.length:
            current = self.head
            while current.get_pointer() != None:
                current = current.get_pointer()
            current.set_pointer(Node(value, None))
        else:
            counter = 1
            tmp = self.head   
            prev = self.head
            while counter !=  pos:
                prev = tmp
                tmp = tmp.get_pointer()
                counter += 1
            new_node = Node(value, None)
            prev.set_pointer(new_node)
            new_node.set_pointer(tmp)
        self.length = self.length + 1  
    
    def delete(self, pos):
        if pos < 1 or pos > self.length:
            raise ValueError("position is not suitable")
        if pos == 1:
            tmp = self.head.get_pointer()
            self.head = tmp
        
        elif pos == self.length:
            current = self.head
            prev = self.head
            while current.get_pointer() != None:
                prev = current
                current = current.get_pointer()
            prev.set_pointer(None)
        else: 
            current = self.head
            prev = self.head
            counter = 1
            while counter != pos:
                prev = current
                current = current.get_pointer()
                counter += 1
            tmp = current.get_pointer()
            prev.set_pointer(tmp)
        self.length -= 1
            
            
            