['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','R','T','Y','P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']





from functools import reduce
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))



'''  GCD  '''
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

l={1,2,3}
[*b,]=l
print(b)
print('='*30)
def keyword_only(*items, _list, default = False):
    print(items)
    print(_list)
    print(default)

nums = [i ** 2 for i in range(1, 6)]
## calling the function
keyword_only(1, 2, 3, 4, 5, _list = nums, default = True)
