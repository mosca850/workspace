'''
Created on 20 Nov 2012

@author: luca
'''
class Error(Exception):
    pass

class LexicalError(Error):
    '''
    classdocs
    '''
    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg
        