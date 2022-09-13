import  SyntaxCheck as SC
class TreeNode:
    def __init__(self,tag,Function,Category,treenode,feature=None,leave=None,Next=None,kids=None,parent=None):
        self.tag=tag
        self.Function = Function
        self.Category = Category
        self.kids=kids
        self.Next=Next
        self.feature=feature
        self.leave=leave
        self.treenode=treenode
        self.parent=parent
        self.kids=kids
        self.Next=Next


def printTree(Tree:TreeNode):
    for i in Tree:
        print(i.treenode+'[')
        if (i.parent):
            print('parent='+i.parent.treenode)
        print('Fuction='+i.Function)
        if(i.feature==None and i.leave==None):
            print('Category=' + i.Category+']\n')
        else:
            print('Category=' + i.Category)
        if(i.feature):
            for j in range(len(i.feature)):
                if(j==len(i.feature)-1 and i.leave==None):
                    print('Feature'+str(j)+'='+i.feature[j]+']\n')
                else:
                    print('Feature' + str(j) + '=' + i.feature[j])
        if(i.leave):
            print('leave='+i.leave+']\n')

def printSentence(Tree:TreeNode):
    queue=[]
    head=Tree[0]
    queue.append(head)
    while(len(queue)!=0):
        size=len(queue)
        for i in range(size):
            if(queue[i].leave):
                print(queue[i].leave,end=' ')
        for i in range(size):
            if(queue[i].kids!=None):
                queue.append(queue[i].kids)
                L=queue[i].kids.Next
                while(L!=None):
                    queue.append(L)
                    L=L.Next
        for i in range(size):
                queue.pop(0)

def reArrangeTree(Tree:TreeNode):
    queue=[]
    LayerNumber = 0
    head=Tree[0]
    queue.append(head)
    while(len(queue)!=0):
        size=len(queue)
        for i in range(size):
            if(queue[i].kids!=None):
                queue.append(queue[i].kids)
                L=queue[i].kids.Next
                while(L!=None):
                    queue.append(L)
                    L=L.Next
        for i in range(size):
                queue[0].tag=LayerNumber
                queue.pop(0)
        LayerNumber=LayerNumber+1

def reStoreTree(Tree:TreeNode,line:str):
    RestoreFile='ReStore.txt'
    f=open(RestoreFile,'a+')
    f.writelines(line)
    for i in range(len(Tree)):
        space=' '*(Tree[i].tag)
        feature=''
        if(Tree[i].feature!=None):
            for j in Tree[i].feature:
                feature=feature+j+','
            feature=feature[0:-1]
        if(Tree[i].leave==None):
            NewNode=space+Tree[i].Function+' '+Tree[i].Category+'('+feature+')\n'
        else:
            NewNode =space+Tree[i].Function + ' ' + Tree[i].Category + '(' + feature + ')'+' '+'{'+Tree[i].leave+'}\n'
        f.writelines(NewNode)
    f.writelines('\n')
    f.close()

def finishTree(Tree:TreeNode):
    size=len(Tree)
    for i in range(size):
        for j in range(size-i-2,-1,-1):
            if(Tree[size-1-i].Function=='PUNC'):
                L=Tree[j].Next
                Tree[j].Next=Tree[size-1-i]
                Tree[size - 1 - i].Next=L
                break
            else:
                if(Tree[j].tag+1<=Tree[size-1-i].tag):
                    Tree[size - 1 - i].parent = Tree[j]
                    if (Tree[j].kids == None):
                        Tree[j].kids = Tree[size - 1 - i]
                        break
                    else:
                        L = Tree[j].kids
                        Tree[j].kids = Tree[size - 1 - i]
                        Tree[j].kids.Next = L
                        break


def  main(address:str):
    f = open(address)
    line = f.readline()
    if(line=='\n'):
        print(1)
    Tree=[]
    AllTree=[]
    ErrorDict = []
    LineNumber=1
    title=[]
    while line:
        if('<#' in line ):
            title.append(line)
            if(len(Tree)!=0):
                finishTree(Tree)
                reArrangeTree(Tree)
                AllTree.append(Tree)
                #printSentence(Tree)
                #print('\n')
                #printTree(Tree)
                reStoreTree(Tree,title[0])
                title.pop(0)
                #print('*'*50)
                while(len(Tree)!=0):
                    Tree.pop()
        elif('<#' not in line and line!='\n' ):
            TmpLine=line
            tmp=TmpLine.split(' ')
            tag=0
            for i in tmp:
                if(i==''):
                    tag=tag+1
                else:
                    break
            islegal = SC.isSyntax(TmpLine)
            if (islegal < 0):
                if (islegal == -1):
                    ErrorDict.append([LineNumber, -1, line])
                elif (islegal == -2):
                    ErrorDict.append([LineNumber, -2, line])
                elif (islegal == -3):
                    ErrorDict.append([LineNumber, -3, line])
            line = line.split('\n')[0]
            Function = line.split()[0]
            Category = 'SubstituteCategory'
            Feature = None
            Leaves = None
            if (len(line.split()) > 1):
                Category = line.split()[1].split('(')[0]
            if ('(' in line):
                if (len(line.split('(')[1])!=0):
                    tmp = line.split('(')[1].split(')')[0]
                    if (len(tmp) > 0):
                        Feature = tmp.split(',')
            if (')'in line and len(line.split(')')[1])!=0):
                if ('{' in line.split(')')[1]):
                    if (len(line.split('{')) > 1):
                        Leaves = line.split('{')[1].split('}')[0]
                else:
                        Leaves = line.split(')')[1].split('}')[0]
            else:
                if (len(line.split('{')) > 1):
                    Leaves = line.split('{')[1].split('}')[0]
            ans= TreeNode(tag=tag,Function=Function, Category=Category, treenode=line, feature=Feature, leave=Leaves)
            Tree.append(ans)
        line = f.readline()
        LineNumber=LineNumber+1
    if (len(Tree) != 0):
        finishTree(Tree)
        reArrangeTree(Tree)
        AllTree.append(Tree)
        reStoreTree(Tree, title[0])
        title.pop(0)
        while (len(Tree) != 0):
            Tree.pop()
    f.close()
    if(len(ErrorDict)!=0):
        print('These line may have problem\n')
        for i in ErrorDict:
            print(i[0],i[1],i[2])


if __name__ == '__main__':
    FileAddress="test.txt"
    main(FileAddress)
