'''
Created on 20 Nov 2012

@author: luca
'''

class Token_lst(list):
    def __init__(self):
        list.__init__(self)
    
    def append(self, *args, **kwargs):
        return list.append(self, *args, **kwargs)
        
        