#!/usr/bin/python3
from optparse import OptionParser
import tree
import Token_lst
from class_def import ClassDef
from tree import Tree
from exceptions import LexicalError
(_ROOT,_DEPTH, _WIDTH) = range(3)
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)
    
    def add_token(self,token,index):
        self.data.append(token)

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
              help="write report to FILE", metavar="FILE")
    #parser.add_option("-q", "--quiet",
    #   action="store_false", dest="verbose", default=True,
    #  help="don't print status messages to stdout")
    (options, args) = parser.parse_args()
    #if options.filename=='':
    options.filename='Test.java'
    ignore_char=['\t','\r'];
    #print(options.filename)
    f=open(options.filename)
    lines=f.readlines()
    tokens=Token_lst.Token_lst()
    special_tokens=[';',':','{','}','(',')',',','[',']','/','\\','*','=','+','-','$','%','>','<','!','~','^','?','.',"'"]
    operators_multiple=['++','--','==','-~','<=','>=','!=','*=','/=','%=','+=','-=','&=','^=','|=','<<=','>>=','>>>=']
    operators_ambiguous=['>>','<<']
    comments=['/*','//']
    assignement_operators=[]
    is_string=False
    spec_char=False
    comment_line=False
    comment=False
    #TODO create a class Token_list that extends list to manage the tokens inserted, in order to sanitize and to not have duplicates.
    for line in lines:
        token=''
        for i in ignore_char:
            line=line.replace(i,'')
        for letter in line:
            if letter == '"':
                if is_string:
                    is_string=False
                    tokens.append(token+letter)
                    token=''
                else:
                    spec_char=False;
                    tokens.append(token)
                    is_string=True
                    token=letter
            elif letter not in special_tokens or is_string:
                if spec_char:
                    spec_char=False;
                    tokens.append(token)
                    token=letter
                else:
                    token+=letter
            else:
                if spec_char:
                    if token+letter in operators_multiple:
                        token+=letter
                        tokens.append(token)
                        token=''
                        spec_char=False
                    elif token+letter in operators_ambiguous:
                        token+=letter
                    else:
                        tokens.append(token)
                        token=letter
                else :
                    tokens+=token.split(" ")
                    token=letter
                    spec_char=True
        if is_string:
            raise LexicalError(token,"Uncorrect String")
        if(token!=''):
            tokens.append(token)
    #text_document=text_document.strip()
    delimiters=[';',':','{','}','(',')',',','[',']','//','\n','/*','*/','.']
    operators=['=','+','-','$','%','*','>','<','!','~','^','?',':']
    operators_double=['++','--','==','-~','<=','>=','!=']
    assignement_operators=['*=','/=','%=','+=','-=','<<=','>>=','>>>=','&=','^=','|='];
    class_found=False
    classes=[]
    line=[]
    tree=[]
    index=0
    node_number=0
    parenthesis_index=0
    for token in tokens:
        if token in ['//']:
            print(token)
            comment_line=True    
        elif token in ['/*']:
            print(token)
            comment=True    
        elif comment_line and token in ['\n']:
            print(token)
            comment_line=False;
        elif token in ['\n']:
            pass
        elif comment and token in ['*/']:
            print(token)
            comment=False
        elif class_found:
                    if token in ['{']:
                        parenthesis_index+=1
                    elif token in ['}']:
                        parenthesis_index-=1
                        if parenthesis_index is 0:
                            print("end of the class")
                            print(classes[-1].toString())
                            if not classes[-1].getType() =='' and not classes[-1].getName()+'.java'== options.filename:
                                classes[-1].error(options.filename,'filename and class name mismatch '+options.filename+' '+classes[-1].getName())
                            class_found=False
                    if token not in ['\n']:
                        classes[-1].addToken(token)
        elif not comment and not comment_line:
            if token not in ['\\n']:
                line.append(token)
            if token in [';']:
                #albero.create_node(line,'node'+str(node_number),parent = index)
                parenthesis_index+=1
                #tree[index].append(line)
                node_number+=1
                ##print(line)
                line=[]
            if token in ['{']:
                class_found=True
                classes.append(ClassDef(line))
                # tree[index].append([line])
                line=[]
                parenthesis_index=1
    for token in tokens:
        print(token);            
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
