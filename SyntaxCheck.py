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
    if(len(tmp[1])==0 or tmp[1][-1]!=')'):
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

def isLeaves(node_split:str)->bool: #{}
    ns=node_split
    length=len(ns)
    punc = string.punctuation
    punc=punc+'”“！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.'
    if(ns[0]!='{' or ns[length-1]!='}'):
        return False
    for i in range(1,length):
        if(ns[i] in punc or str.isalnum(ns[i]) or ns[i]==' '):
            continue
        else:
            return False
    return True


def isSyntax(node:str)->int:
    s=node.split('\n')[0]
    tmp=s.split()
    tmp1=tmp[0]
    tmp2=tmp[1]
    if('{'in s ):
        tmp3='{'+s.split('{')[1]
        if (isLeaves(tmp3) == False):
            return -3
    if(isFunction(tmp1)==False):
        return -1
    if(isCatergory(tmp2)==False or len(tmp2)==0):
        return -2
    return 1




