q=w=[1,2,3]
q[0]=3
print(q,w)


##############


q=[[]]*3
q[0].append(1)
print(q)


##############


x=[1,2]
y=[x]*2
print(y,x,'='*20,sep='\n')


x[0]='w'
print(y,x,'='*20,sep='\n')


y[0][0]='q'
print(y,x,'='*20,sep='\n')


##################################


x=[1,2]
y=[list(x)]*2
print(y,x,'='*20,sep='\n')


x[0]='w'
print(y,x,'='*20,sep='\n')


y[0][0]='q'
print(y,x,'='*20,sep='\n')


##################################


