import string

ErrorDict=[]
def isFunction(node_split:str)->bool:
    for i in node_split:
        if(str.isalnum(i)):
            continue
        else:
            return False
    return True

def isCatergory(node_split:str)->bool:
    ns=node_split
    tmp=ns.split('(')
    if(len(tmp)==1 or tmp[1][-1]!=')'):
        return False
    for i in tmp[0]:
        if(str.isalnum(i)  ):
            continue
        else:
            return False
    for i in range(len(tmp[1])-1):
        if(str.isalnum(tmp[1][i])or tmp[1][i]==','or tmp[1][i]=='-'):
            continue
        else:
            return False
    return True




def isSyntax(node:str)->int:
    s=node.split('\n')[0]
    tmp=s.split()
    tmp1=tmp[0]
    tmp2='SubstituteCategory'
    if(len(tmp)>1):
        tmp2=tmp[1]
    if(isFunction(tmp1)==False):
        return -1
    if(len(tmp2)=='SubstituteCategory' or isCatergory(tmp2)==False ):
        return -2
    tmp3=s.split(')')[1]
    if(len(tmp3)!=0 or '{'in s or'}' in s):
        if(not(len(tmp3)!=0 and '{'in s and'}' in s)):
            return -3
    return 1




