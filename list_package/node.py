# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 18:14:58 2018

@author: Ulukbek Attokurov
"""

class Node:
    def __init__(self, value = None, pointer = None):
        self.value = value
        self.pointer = pointer
    
    def get_value(self):
        return self.value
    
    def set_value(self, new_value):
        self.value = new_value
        
    def get_pointer(self):
        return self.pointer
    
    def set_pointer(self, pointer):
        self.pointer = pointer
    

        