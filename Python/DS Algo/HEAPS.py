from heapq import *

'''

        heapify(#)
        heappush(#,ele)
        heappop(#)
        heappushpop(#,ele)  ##--First push then pop, popped ele can be stored
                            ##--The heappushpop() action runs more efficiently than
                                heappush() followed by a separate call to heappop().
        heapreplace(#,ele)  ##--First pop then push, popped ele can be stored
                            ##--If the heap is empty, IndexError is raised.
        nlargest(k,#,key=fun)
        nsmallest(k,#,key=fun)
                            ##--If repeated usage of these functions is required,
                                consider turning the iterable into an actual heap.
        merge(*#)           ##--convert into list

'''

################################################################################


def kth_smallest(l,k):
    m=len(l)
    h=l[:m-k+1]
    heapify(h)
    for i in range(m-k+1,m):
        heappushpop(h,l[i])
        '''if nsmallest(1,h)[0]<l[i]:
                heapreplace(h,l[i])'''
    return h[0]


################################################################################


def kth_largest(l,k):
    m=len(l)
    h=l[:k]
    heapify(h)
    for i in range(k,m):
        '''if nsmallest(1,h)[0]<l[i]:
            heapreplace(h,l[i])'''
        heappushpop(h,l[i])
    return h[0]


################################################################################


def k_smallest(l,k):
    m=len(l)
    h=l[:m-k]
    heapify(h)
    q=[]
    heapify(q)
    for i in range(m-k,m):
        heappush(q,heappushpop(h,l[i]))
    return nsmallest(k,q)


################################################################################


def k_largest(l,k):
    m=len(l)
    h=l[:k]
    heapify(h)
    for i in range(k,m):
        heappushpop(h,l[i])
    return nsmallest(k,h)
l=sorted([5,10,3,12,15,9,17,2])
for i in range(8):
    print('for i={} '.format(i))
    print(k_smallest([5,10,3,12,15,9,17,2],i+1))
    print(l[:i+1])

##l=sorted([5,10,3,12,15,9,17,2])
