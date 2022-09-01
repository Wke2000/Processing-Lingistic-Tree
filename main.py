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
            if(Tree[j].tag+1==Tree[size-1-i].tag):
                Tree[size-1-i].parent=Tree[j]
                if(Tree[j].kids==None):
                    Tree[j].kids=Tree[size-1-i]
                    break
                else:
                        L=Tree[j].kids
                        Tree[j].kids=Tree[size-1-i]
                        Tree[j].kids.Next=L
                        break


def  main(address:str):
    f = open(address)
    line = f.readline()
    Tree=[]
    AllTree=[]
    while line:
        if('<#w2c-' in line ):
            if(len(Tree)!=0):
                finishTree(Tree)
                AllTree.append(Tree)
                printSentence(Tree)
                print('\n')
                printTree(Tree)
                print('*'*50)
                while(len(Tree)!=0):
                    Tree.pop()
        elif('<#w2c-' not in line ):
            tmp=line.split(' ')
            tag=0
            for i in tmp:
                if(i==''):
                    tag=tag+1
                else:
                    break
            tmp=line.split()
            if(tmp==[]):
                line = f.readline()
                continue
            tmp1=tmp[1].split('(')[0]
            if('(' in line):
                tmp2=tmp[1].split('(')[1].split(')')[0]
            else:
                tmp2=''
            tmp3=None
            if(len(tmp)>2):
                tmp3=line.split('{')[1].split('}')[0]
            if(len(tmp2)>0):
                tmp2=tmp2.split(',')
                ans=TreeNode(tag=tag,Function=tmp[0],Category=tmp1,treenode=line.split('\n')[0],feature=tmp2,leave=tmp3)
            else:
                ans=TreeNode(tag=tag,Function=tmp[0],Category=tmp1,treenode=line.split('\n')[0],leave=tmp3)

            Tree.append(ans)
        line = f.readline()
    f.close()

if __name__ == '__main__':
    FileAddress="C://Users//86153//Desktop//w2c-001.syn"
    main(FileAddress)