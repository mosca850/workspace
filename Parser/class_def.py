import uuid, sys


class Import:

    def __init__(self,path, identifier=None):
        self.__identifier = (str(uuid.uuid1()) if identifier is None else str(identifier))
        self.path = path 

class InvalidType(Exception):
    """Exception raised for errors in the input.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg

class ClassDef:
    class_types=['public','protected','private','abstract','static','final','strictfp']
    def __init__(self,line):
        self.type=''
        self.name=''
        self.methods=[]
        self.code=[]
        self.extension=''
        self.implementations=[]
        print(line)
        index=0
        if line[index] in self.class_types:
            self.type=line[index]
            index+=1
        if line[index] not in ['class']:
            self.error(line[index],'syntax error next to '+line[index])
        index+=1
        self.name= line[index]
        extends=False
        implements=False
        index+=1
        while index<len(line)-1:
            if line[index] == 'extends' and not extends:
                self.extension=line[index+1]
            elif line[index] =='implements' and not implements:
                self.implementations.append(line[index+1])
                implements=True
                while index+2<len(line) and line[index+2] == ',':
                    index+=2
                    if index+2>=len(line):
                        self.error(line[index+1],'implementation error '+line[index+1])
                    else:
                        self.implementations.append(line[index+1])
            else:
                self.error(line[index],'extension error '+line[index])
            extends=True
            index+=2
    def addToken(self,token):
        self.code.append(token)

    def toString(self):
        print(self.name+' '+ self.type)
        print('extends',self.extension,'implements',self.implementations)
    
    def addMethod(self,method):
        self.methods.append(Method(method))
        print(method)
    def addConstructor(self,code):
        print('CONSTRUCTOR!!!!!!!!!!!!',code)
    def error(self,token,error_message):
        try:
            raise InvalidType(token,error_message)
        except InvalidType as e:
            print(error_message)
            sys.exit(2)
    def getLastMethod(self):
        return self.methods[-1]
    def analyzeCode(self):
        ##division of variables methods and constructor
        parenthesis_index=0
        method_found=False
        methods=list()
        for token in self.code:
            if token in ['}']:
                parenthesis_index-=1
                if parenthesis_index is 0:
                    method_found=False
                    if token not in ['\\n']:
                        methods[-1].addToken(token)
                if token not in ['\\n']:
                    line.append(token)
                if token in [';']:
                    albero.create_node(line,'node'+str(node_number),parent = index)
                    parenthesis_index+=1
                    tree[index].append(line)
                    node_number+=1
                    line=[]
                if token in ['{']:
                    class_found=True
                    classes.append(ClassDef(line))
                    albero.create_node(line,index+1,parent = index)
                    tree.append([line])
                    line=[]
                    parenthesis_index=1
    def getName(self):
        return self.name
    def getType(self):
        return self.type
            
class Method:
    method_types=['public','protected','private','abstract','static','final','synchronized','native','strictfp']
    def __init__(self,meth_def):
        self.code=[]
        self.return_type=''
        self.type=''
        self.name=''
    def addToken(self,token):
        self.code.append(token)

class Constructor:
    method_types=['public','protected','private']
    def __init__(self,type,name,return_type,code=None):
        self.code=[]
        self.return_type
        self.type=type
        self.name=name
    def addCode(self,code):
        self.code=code
        
if __name__ == "__main__":
    class_test=ClassDef('private')
    class_test.toString()
