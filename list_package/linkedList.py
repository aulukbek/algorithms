# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:24:51 2018

@author: Ulukbek Attokurov
"""

# -*- coding: utf-8 -*-

from node import Node
"""
    Linked list is implemented using private methods 
    - header of the list is stored as a private variable 
"""
class LinkedList:     
    def __init__(self, value, pointer):
        self.__head = Node(value, pointer)
        self.__length = 1  
    
    def __len__(self):
        return self.__length
    
    def __getitem__(self, pos):
        if (pos > self.__length) or (pos < 1):
            raise ValueError("position is not suitable")
        counter = 1
        tmp = self.__head
        while counter != pos:
            tmp = tmp.get_pointer()
            counter += 1
        return tmp  
    
    def __insertStart(self, value):
        if not self.__head:
            self.__head = Node(value, None)
        else:
            tmp = self.__head
            self.__head = Node(value, tmp)
    
    def __insertEnd(self, value):
        tmp = self.__head
        while tmp.get_pointer():
            tmp = tmp.get_pointer()
        new_node = Node(value, None)
        tmp.set_pointer(new_node)
        
    def __insertMiddle(self, value, pos):
        if pos > self.__length or pos < 1:
            raise ValueError("position is wrong")
        counter = 1
        tmp = self.__head
        prev = tmp
        while counter != pos:
            prev = tmp
            tmp = tmp.get_pointer()
            counter += 1
        new_node = Node(value, None)
        new_node.set_pointer(tmp)
        prev.set_pointer(new_node)
        
    def insert(self, value, pos):
        if self.__length < pos or pos < 1:
            raise ValueError("position is not suitable")
        if pos == 1:
            self.__insertStart(value)
        elif pos == self.__length:
            self.__insertEnd(value)
        else:
            self.__insertMiddle(value, pos)
        self.__length += 1
        
    def traverse(self):
        tmp = self.__head
        counter = 1
        while tmp:
            print "postion is ", counter
            print "value is ", tmp.get_value()
            tmp = tmp.get_pointer()
            counter += 1
        
    def delete(self, pos):
        if pos < 1 or pos > self.__length:
            raise ValueError("position is not suitable")
        if pos == 1:
            tmp = self.__head.get_pointer()
            self.__head = tmp
        
        elif pos == self.__length:
            current = self.__head
            prev = self.__head
            while current.get_pointer() != None:
                prev = current
                current = current.get_pointer()
            prev.set_pointer(None)
        else: 
            current = self.__head
            prev = self.__head
            counter = 1
            while counter != pos:
                prev = current
                current = current.get_pointer()
                counter += 1
            tmp = current.get_pointer()
            prev.set_pointer(tmp)
        self.__length -= 1
            
            
            

