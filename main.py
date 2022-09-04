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


def printTree(stree:TreeNode):
    Tree=stree
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

def printSentence(sTree:TreeNode):
    Tree=sTree
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

def finishTree(sTree:TreeNode):
    Tree=sTree
    size=len(Tree)
    for i in range(size):
        for j in range(size-i-2,-1,-1):
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
    while line:
        if('<#' in line ):
            if(len(Tree)!=0):
                finishTree(Tree)
                AllTree.append(Tree)
                printSentence(Tree)
                print('\n')
                printTree(Tree)
                print('*'*50)
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
            islegal=SC.isSyntax(TmpLine)
            if(islegal<0):
                if(islegal==-1):
                    ErrorDict.append([LineNumber,-1,line])
                    TmpLine=' '*tag+SC.AlternateNodes_1
                elif (islegal == -2):
                    ErrorDict.append([LineNumber, -2, line])
                    TmpLine = ' '*tag+SC.AlternateNodes_2
                elif (islegal == -3):
                    ErrorDict.append([LineNumber, -3, line])
                    TmpLine = ' '*tag+SC.AlternateNodes_3
            tmp=TmpLine.split()
            NodeFuction=tmp[0]
            NodeCategory=tmp[1].split('(')[0]
            NodeTreeNode=TmpLine.split('\n')[0]
            NodeFeature=tmp[1].split('(')[1].split(')')[0]
            if (len(NodeFeature) == 0):
                NodeFeature = None
            else:
                NodeFeature = NodeFeature.split(',')
            if('{' in line):
                NodeLeaves= TmpLine.split('{')[1].split('}')[0]
            else:
                NodeLeaves=None

            ans=TreeNode(tag,NodeFuction,NodeCategory,NodeTreeNode,NodeFeature,NodeLeaves)
            Tree.append(ans)
        line = f.readline()
        LineNumber=LineNumber+1
    f.close()
    if(len(ErrorDict)!=0):
        print('These line may have problem\n')
        for i in ErrorDict:
            print(i[0],i[1],i[2])

if __name__ == '__main__':
    FileAddress='test.txt'
    main(FileAddress)
