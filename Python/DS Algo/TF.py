class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.depth=None
class hdcr:
    def __init__(self):
        self.head=None
def insrt(h,k):
    if h==None:
        return Node(k)
    if k<h.data:
        h.left=insrt(h.left,k)
    else:
        h.right=insrt(h.right,k)
    return h
def preO(h):
    if h==None:
        return
    print(h.data,end=' ')
    preO(h.left)
    preO(h.right)
def inO(h):
    if h==None:
        return
    inO(h.left)
    print(h.data,end=' ')
    inO(h.right)
def postO(h):
    if h==None:
        return
    postO(h.left)
    postO(h.right)
    print(h.data,end=' ')
def size(h):
    if h==None:
        return 0
    return 1+size(h.left)+size(h.right)
def Sum(h):
    if h==None:
        return 0
    return h.data+Sum(h.left)+Sum(h.right)
def Max(h):
    if h==None:
        return inf
    return max(h.data,Max(h.left),Max(h.right))
def height(h):
    if h==None:
        return -1
    return 1+max(height(h.left),height(h.right))
def mirror(h):
    if h==None:
        return
    mirror(h.left)
    mirror(h.right)
    h.left,h.right=h.right,h.left
n=lambda:map(int,input().split())
t=[*n(),][0]
while t>0:
    m=[*n(),][0]
    e=[*n(),]
    l=hdcr()
    for i in e:
        l.head=insrt(l.head,i)
    preO(l.head)
    mirror(l.head)
    preO(l.head)
    t-=1
