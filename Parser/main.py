#!/usr/bin/python3
import argparse
import tree,class_def
import uuid, sys
from class_def import ClassDef
from tree import Tree
(_ROOT,_DEPTH, _WIDTH) = range(3)
class InvalidType(Exception):
    """Exception raised for errors in the input.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)
    
    def add_token(self,token,index):
        self.data.append(token)
def getTokens(text_document):
    text_document=text_document.strip()
    delimiters=[';',':','{','}','(',')',',','[',']','//','\n','/*','*/']
    for d in delimiters:
        text_document=text_document.replace(d,' '+d+' ')
    for i in ignore_char:
        text_document=text_document.replace(i,'')
    #text_document.replace('= =','==')
    #text_document.replace('\n','\\n')
    text_document=repr(text_document)
    return text_document.split()
def error(token,error_message):
    try:
        raise InvalidType(token,error_message)
    except InvalidType as e:
        print(error_message)
        sys.exit(2)
def isMethod(def_tokens,class_name):
    if len(def_tokens)<4:
        error('IsMethod','unknown sequence of tokens'+str(def_tokens))
    elif def_tokens[0] in ['public', 'protected', 'private']:
        if def_tokens[1]==class_name:
            return False
    elif def_tokens[0]==class_name:
        return False
    return True
if __name__ == "__main__":
    parser=argparse.ArgumentParser(description='Process Arguments.')
    parser.add_argument("-f", "--file", type=str,dest="filename",default='Test.java',
              help="write report to FILE", metavar="FILE")
    #parser.add_option("-q", "--quiet",
    #   action="store_false", dest="verbose", default=True,
    #  help="don't print status messages to stdout")
    (options) = parser.parse_args()
    ignore_char=['\t','\r'];
    if len(options.filename)<6 or options.filename[len(options.filename)-5:len(options.filename)] !='.java':
        error(options.filename,'this is not a java file '+options.filename)

    f=open(options.filename)
    tokens=getTokens(f.read())
    tree=[[]]
    index=0
    node_number=0
    line=[]
    comment_line=False
    comment=False
    class_found=False
    method_found=False
    constructor_found=False
    classes=[]
    parenthesis_index=0
    for token in tokens:
        if token in ['//']:
            print(token)
            comment_line=True    
        elif token in ['/*']:
            print(token)
            comment=True    
        elif comment_line and token in ['\\n']:
            print(token)
            comment_line=False;
        elif comment and token in ['*/']:
            print(token)
            comment=False;
        elif class_found:
            if token not in ['\\n']:
                if method_found:
                    classes[-1].getLastMethod().addToken(token)
                elif constructor_found:
                    classes[-1].getLastConstructor.addToken(token)
                else:
                    line.append(token)
            if token in ['{']:
                parenthesis_index+=1
                if isMethod(line,classes[-1].getName()):
                    method_found=True
                    classes[-1].addMethod(line)
                else:
                    constructor_found=True
                    classes[-1].addConstructor()
            elif token in ['}']:
                constructor_found=False
                method_found=False
                parenthesis_index-=1
                if parenthesis_index is 0:
                    print("end of the class")
                    classes[-1].toString()
                    if not classes[-1].getType() =='' and not classes[-1].getName()+'.java'== options.filename:
                        classes[-1].error(options.filename,'filename and class name mismatch '+options.filename+' '+classes[-1].getName())
                    class_found=False
        elif not comment and not comment_line:
            if token not in ['\\n']:
                line.append(token)
            if token in [';']:
                parenthesis_index+=1
                tree[index].append(line)
                node_number+=1
                ##print(line)
                line=[]
            if token in ['{']:
                class_found=True
                classes.append(ClassDef(line))
                tree.append([line])
                line=[]
                parenthesis_index=1
    
"""
            if token in ['}']:
                index-=1
            line.append(token)
            if token in [';']:
                albero.create_node(line,'node'+str(node_number),parent = index)
                tree[index].append(line)
                node_number+=1
                print(line)
                line=[]
            if token in ['{']:
                albero.create_node(line,index+1,parent = index)
                tree.append([line])
                line=[]
                index+=1
    for bone in tree:
        print(bone)
        print('>>>>>>>>>>>>>>>>>>>>>>')
"""
