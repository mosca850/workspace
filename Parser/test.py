class Token:
    IDENTIFIER=1
    NUMBER=2
    KEYWORD=3
    LITERAL=4
    DATATYPE=5
    OPERATOR=6
    STRING=7
    SEPARATOR=8
    PARENTHESIS=9
    def __init__(self,value):
        self.value=value
    def setType(self,type):
        self.type=type
"""
if __name__ == "__main__":
    class_test=ClassDef('private')
    class_test.toString()
"""
