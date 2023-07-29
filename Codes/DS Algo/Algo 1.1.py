u=lambda:map(int,input().split())


'''
    Maximum Product Subarray
    TC : O(N)
    SC : O(N)
    YouTube Link : https://www.youtube.com/watch?v=vtJvbRlHqTA
    [-1, 6, 2, 0, 7, 9]
'''

def max_prdt_subarr():
    l=[*u(),]
    t=l[0]
    cm,cn,z,pm,pn=t,t,t,t,t
    for i in l[1:]:
        cm=max(pm*i,pn*i,i)
        cn=min(pm*i,pn*i,i)
        z=max(cm,z)
        pm,pn=cm,cn
    return z


################################################################################


'''
    Count the no of Triangles in the given level
    SPOJ : Count the Triangles
    TC : O(N+T)
    SC : O(N)
'''

def count_the_triangles():
    t=int(input())
    q=[]
    m=-1
    for _ in range(t):
        q.append(int(input()))
        m=max(m,q[-1])
    s,o,e,t,i=0,0,0,0,1
    l=[1]
    while i<=m:
        t+=i
        s+=t
        if i%2!=0:
            o+=t
            l.append(s+e)
        else:
            e+=t
            l.append(s+o)
        i+=1
    for i in q:
        print(l[i])


################################################################################


'''
    Adding all the no's upto N by its binary
    InfyTQ : Sum of binary and decimal numbers
    TC : No. of bits in the no.
    SC : Binary Representation

    Eg : 1=1,2=11,3=22,4=122,5=223,6=333.....
'''

def add_as_bits(n):
    ' default if n==1 : 1 process from 2'
    s=bin(n)[2:]
    t=0
    m=len(s)
    a=2**(m-2)
    l=[0]*m
    for i in range(m):
        if s[i]=='1':
            n-=2**(m-(i+1))
            l[-m+i]+=t+1+n   #n==int('0b'+s[i+1:],2)
            t+=a
        else:
            l[-m+i]+=t
        a//=2
    print(l)


" Remarks : Can use this - int('0b'+s[i+1:],2)...but check if empty string('')  "
"            is passed it shows error   "


##################################################################################


'''
    Least next no to the rightside of the no
    APT : Notes Phase-2 Day-4
    TC : O(N)
    SC : O(N)
    Test Cases
    n=10
    l=[10,15,12,18,20,16,14,8,25,13]
    a=[8,12,8,16,16,14,8,-1,13,-1] #Answer
'''
def from_start(l,n):
    p=[]
    q=[-1]*n
    for i in range(n):
        #print(i)
        while p!=[] and l[p[-1]]>l[i]:
            q[p[-1]]=l[i]
            p.pop()
        p.append(i)
    return q


def from_end(l,n):
    p=[]
    q=[-1]*n
    for i in range(n-1,-1,-1):
        while p!=[] and l[p[-1]]>l[i]:
            p.pop()
        if p!=[]:
            q[i]=l[p[-1]]
        p.append(i)
    return q


######################################################################################

'''
Sieve_of_Eratosthenes
for generating prime numbers
ideally we generate 10**6
'''


def Sieve_of_Eratosthenes(n):
    #n=10**6+1

    l=[0]*n
    p=[]

    for i in range(2,n):
        
        if l[i]==0:
            p.append(i)
            j=i*i
            while j<n:
                l[j]=1
                j+=i
    return p



'''
Insertion Sort
SI Prac : Insertion Sort Adhoc, Page-4 : 10, 
'''

n=lambda:map(int,input().split())
t=[*n(),][0]
while t>0:
    m=[*n(),][0]
    l=[*n()]
    z=0
    for i in range(1,m):
        k=l[i]
        j=i-1
        while j>=0 and k<l[j] : 
                l[j+1]=l[j] 
                j-=1
        l[j+1]=k
        print(j+1,end=' ')
    print()
    t-=1



'''
A power B
SI Prac : Compute a power b , Page-3 : 3, 
APT : Day-3,
'''

g=1000000007
n=lambda:map(int,input().split())
t=[*n(),][0]
while t>0:
    a,b=[*n(),]
    x=a
    ans=1
    while(b!=0):
        if b&1:
            ans=(ans*x)%g
        x=(x*x)%g
        b=b>>1
    print(ans%g)
    t-=1




def GCD(a,b):
    while b:
        a,b=b,a%b
    return a




'''
Collecting Water (or) Builiding water
SI Prac : Page-10 : 10
'''

def collecting_water(l):
    n=len(l)
    ML=[l[0]]
    for i in range(1,n):
        ML.append(max(ML[-1],l[i]))
    MR=[0]*n
    MR[-1]=l[-1]
    for i in range(n-2,-1,-1):
        MR[i] = max(MR[i+1],l[i])
    
    z=0
    for i in range(1,n-1):
        z+=min(ML[i],MR[i])-l[i]
    
    return z





'''
Tower of Hanoi
All sorting Algos[SS, IS, BS, MS, HS]
Merge A into B
2 pointer
Binary Search
Floor and Ciel of Binary Search
Max subarray SUM
Max non decreasing subarray
Max subarray that is contigious after rearranging w & wt (with & without) duplicates
Distinct elements in a window
Palindrome w & wt DP
Max subarray containing equal no of 0's and 1's
Given rotated array find K
K-rotated array convert to reg array



'''