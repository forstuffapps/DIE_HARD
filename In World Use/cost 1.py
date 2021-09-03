#from itertools import *
#nn=int(input('Total no of items'))
#l=list(map(int,input('Enter the list of items').split()))
#m=int(input('Max value'))
l=[10,11,22,34,12,17,18,16,14,16,21,23,11,20,19]
nn=15
m=50
f=[]
e=10**9+7
def q(t,m,l,f,e):
    s,te=0,0
    for i in t:
        s+=l[i]
        if s>=m:
            te+=s-m
            s=0
    te+=s
    if te<e:
        e=te
        f=list(t).copy()
    
def p_1(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)
def z(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = range(n, n-r, -1)
    q(tuple(pool[i] for i in indices[:r]),m,l,f,e)
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                q(tuple(pool[i] for i in indices[:r]),m,l,f,e)
                break
        else:
            return
z(range(nn))
