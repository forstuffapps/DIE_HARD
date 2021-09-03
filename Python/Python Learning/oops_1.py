class qwe:
    def __init__(self):
        print('default')
        
    def fun(self):
        print('fun')
qwe().fun()
w=qwe()
w.fun()



print('\n'*2,'#'*40,'\n'*2)


class qwe:
    print('just printing empty')
    q=8
    print(8)


print('\n'*2,'#'*40,'\n'*2)


class qwe:
    q=123
    print('non')
    def __init__(self,n):
        self.n=n
        
        
print(qwe(456).n)



print('\n'*2,'#'*40,'\n'*2)



class qwe:
    q=123
    def __init__(self):
        self.v=456
        print(self.q)
        ''' print(q) = Error q not found '''

    def fun(self):
        self.t=789
        print(self.v)
        ''' print(v) = Error q not found '''
        print(self.q)
        ''' print(q) = Error q not found '''

    def fun2(self):
        print(self.t)
        

z=qwe()
z.fun()
z.fun2()



print('\n'*2,'#'*40,'\n'*2)



class qwe:
    pass


''' Empty Class '''
