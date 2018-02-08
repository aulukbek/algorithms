
from node import NodeDouble

class DLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        
    def insertStart(self, value):
        node = NodeDouble(value)
        if not self.__head:            
            self.__head = node
            self.__tail = node
        else:
            tmp  = self.__head
            self.__head = node
            self.__head.setNext(tmp)
            tmp.setPrev(self.__head)
            
            
    def insertAtEnd(self, value):
        node = NodeDouble(value)
        if not self.__head:
            self.__head = node
            self.__tail = node
        else:
            self.__tail.setNext(node)
            node.setPrev(self.__tail)
            self.__tail = node
            
    def __getPlace(self, pos):
        current = self.__head
        prev = self.__head
        idx = 0
        
        while idx < pos and current.getNext():
            prev = current
            current = current.getNext()
            idx += 1
        return current 
            
        
            
    
    def insertAtMiddle(self, value, pos):
        node = NodeDouble(value)
        if pos == 0 and self.__head:
            node.setNext(self.__head)
            self.__head.setPrev(node)
            self.__head = node
        elif pos == 0 and not self.__head:
            self.__head = node
            self.__tail = node
        else:
            current = self.__getPlace(pos)
            current.getPrev().setNext(node)
            node.setPrev(current.getPrev())
            node.setNext(current)
            current.setPrev(node)
        
    def printList(self):
        current = self.__head
        
        while current:
            print current.getValue()
            current = current.getNext()
    
    def printListTail(self):
        current = self.__tail
        while current:
            print current.getValue()
            current = current.getPrev()
            
            
    
            
            
            


