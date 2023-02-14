from math import *
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class hdcr:
    def __init__(self):
        self.head=None
def push(h,k):
    if h==None:
        h=Node(k)
        return h
    h.next=push(h.next,k)
    return h
def display(h):
    while h!=None:
        print(h.data)
        h=h.next
def size_R(h):
    if h==None:
        return 0
    return 1+size(h.next)
def printrev_R(h):
    if h==None:
        return
    printrev(h.next)
    print(h.data)
'''###---
            If you want to print without recurssion, iterate and store in a list
            and then print the list
                                    ---###'''
def insrtSL(h,k):
    kk=Node(k)
    if h==None or k<=h.data:
        kk.next=h
        return kk
    else:
        while h.next!=None and k>h.next.data:
            h=h.next
        kk.next=h.next
        h.next=kk
def delatpos(h,m,p):
    if p<1 or p>m:
        return h
    if p==1:
        return h.next
    th=h
    while p!=2:
        h=h.next
        p-=1
    h.next=h.next.next
    return th
def insrtatpos(h,k,p,m):
    kk=Node(k)
    if p<1 or p>(m+1):
        return h
    if p==1:
        kk.next=h
        return kk
    th=h
    while p!=2:
        h=h.next
        p-=1
    kk.next=h.next
    h.next=kk
    return th
def delall(h,k):
    if h==None:
        return h
    th=h
    while h.next!=None:
        if h.next.data==k:
            h.next=h.next.next
        else:
            h=h.next
    if th.data==k:
        th=th.next
    return th
def distinct(h):
    if h==None:
        return
    th=h
    while h.next!=None:
        if h.data==h.next.data:
            h.next=h.next.next
        else:
            h=h.next
def rev_I(h):
    p=None
    if h==None:
        return h
    while h!=None:
        t=h.next
        h.next=p
        p=h
        h=t
    return p
def rev_R(h):
    if h==None or h.next==None:
        return h
    hh=revR(h.next)
    h.next.next=h
    h.next=None
    return hh
def findMid(h,flag=True):
    s,f=h,h
    while f.next!=None and f.next.next!=None:
        s=s.next
        f=f.next.next
    if f.next==None or flag==True:
        return s
    return s.next
def bs(h):
    if h==None or h.next==None:
        return
    while h.next!=None:
        t=h.next
        while t!=None:
            if h.data>t.data:
                h.data,t.data=t.data,h.data
            t=t.next
        h=h.next
def merge(h1,h2):
    if h1==None:
        return h2
    elif h2==None:
        return h1
    elif h1.data<h2.data:
        h=h1
        h1=h1.next
    else:
        h=h2
        h2=h2.next
    d=h
    while h1!=None and h2!=None:
        if h1.data<h2.data:
            d.next=h1
            h1=h1.next
        else:
            d.next=h2
            h2=h2.next
        d=d.next
    while h1!=None:
        d.next=h1
        h1=h1.next
        d=d.next
    while h2!=None:
        d.next=h2
        h2=h2.next
        d=d.next
    return h
def palindrome(h):
    n=findMid(h)
    t=n
    n.next=revR(n.next)
    n=n.next
    while h!=None and n!=None:
        if h.data==n.data:
            h=h.next
            n=n.next
        else:
            t.next=revR(t.next)
            return False
    t.next=revR(t.next)
    return True
def rearrange(h):
    m=findMid(h)
    sh=m.next
    m.next=None
    sh=revR(sh)
    while h!=None and sh!=None:
        t=sh.next
        sh.next=h.next
        h.next=sh
        h=sh.next
        sh=t
def OddsEvens(h):
    if h==None:
        return h
    dE,dO,tE,tO=None,None,None,None
    while h!=None:
        if int(fabs(h.data))%2==0:
            if dE==None:
                dE=h
                tE=h
            else:
                tE.next=h
                tE=tE.next
        else:
            if dO==None:
                dO=h
                tO=h
            else:
                tO.next=h
                tO=tO.next
        h=h.next
    if dE==None:
        return dO
    elif dO==None:
        return dE
    tO.next=dE
    tE.next=None
    return dO
def unique_R(h,f):
    if h==None or h.next==None:
        return h,False
    h.next,f=unique(h.next,f)
    if h.data==h.next.data:
        h.next=h.next.next
        return h,True
    elif f==True:
        h.next=h.next.next
        return h,False
    else:
        return h,False
    #Don't forget to write this in main execution
'''
        if f:
            l.head=l.head.next
                                    '''
def unique(h):
    th=h
    d={}
    if h==None or h.next==None:
        return h
    while h.next!=None:
        if h.data==h.next.data:
            d[h.data]=1
            h.next=h.next.next
        else:
            if h.data not in d:
                d[h.data]=0
            h=h.next
    else:
        if h.data not in d:
            d[h.data]=0
    '''if th!=None and d[th.data]==1:
        th=th.next'''
    h=th
    while h!=None and h.next!=None:
        if d[h.next.data]==1:
            h.next=h.next.next
        else:
            h=h.next
    if th!=None and d[th.data]==1:
        th=th.next
    return th
def rotate(h,k):
    th=h
    m=size(h)
    k=k%m
    if k<1 or k>m-1 or h==None or h.next==None:
        return h
    m-=1
    while m>k:
        h=h.next
        m-=1
    t=h.next
    l=th
    while l.next!=None:
        l=l.next
    l.next=th
    h.next=None
    return t
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        AA,BB=A,B
        a,b=0,0
        th1=A
        th2=B
        c=0
        while A!=None and B!=None:
            AA,BB=A,B
            A.val=(A.val+B.val+c)
            if A.val>=10:
                c=1
                A.val=A.val%10
            else:
                c=0
            B.val=A.val
            A=A.next
            B=B.next
        while A!=None:
            AA=A
            a=1
            A.val=(A.val+c)
            if A.val>=10:
                c=1
                A.val=A.val%10
            else:
                c=0
            A=A.next
        else:
            if c!=0:
                AA.next=ListNode(c)
        while B!=None:
            BB=B
            b=1
            B.val=(B.val+c)
            if B.val>=10:
                c=1
                B.val=B.val%10
            else:
                c=0
            B=B.next
        else:
            if c!=0:
                BB.next=ListNode(c)
        if a==1:
            return th1
        else:
            return th2
n=lambda:map(int,input().split())
t=[*n(),][0]
while t>0:
    m=[*n(),][0]
    e=[*n(),]
    #l,k,w=hdcr(),hdcr(),hdcr()
    l=hdcr()
    #for i in m:
        #k.head=push(k.head,i)
    for i in e:
        l.head=push(l.head,i)
    l.head=insrtSL(l.head,2)
    display(l.head)
    t-=1
