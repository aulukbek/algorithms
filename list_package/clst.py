

from node import Node

class CircularList:
    def __init__(self): 
        print " a list is initialized"
        self.__head = None      
    
    def insertAtStart(self, value): 
        print "a function insert at start"
        tmp = Node(value)
        if not self.__head:  
            print "a list is empty"
            self.__head = tmp
            self.__head.set_pointer(tmp)
        else:
            last = self.__getLast()
            tmp.set_pointer(self.__head)
            self.__head = tmp            
            last.set_pointer(tmp)
    
    def insertAtEnd(self, value):
        tmp = Node(value)
        if not self.__head:
            self.__head = tmp
            self.__head.set_pointer(tmp)
        else:
            last = self.__getLast()
            last.set_pointer(tmp)
            tmp.set_pointer(self.__head)
            
    def insertAtMid(self, value, pos):
        if pos == 0:
            self.insertAtStart(value)
        else:
            tmp = Node(value)
            current = self.__getPlace(pos)
            current.set_pointer(tmp)
            
    def __getLast(self):
        print "a function get last"
        current = self.__head
        if not current:
            raise ValueError("a list is empty")
        else:
            while current.get_pointer() != self.__head:
                print current.value
                current = current.get_pointer()
        return current
            
    def __getPlace(self, pos):
        current = self.__head
        idx = 0
        prev = current
        while current != self.__head and idx < pos:
            prev = current
            current = current.get_pointer()
            idx += 1
        return prev
        
    def printCl(self):
        print "a function is printCl"
        current = self.__head.get_pointer()
        print "head value is", self.__head.get_value()
        while current != self.__head: 
            print "print cl value is"
            print current.value
            current = current.get_pointer()
            
   
        
        
            
    
            