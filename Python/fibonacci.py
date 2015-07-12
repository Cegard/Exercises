#!/usr/bin/env python
__author__ = "Cegard"


def fibo(n):
    """función iterativa de los n primeros
    números de la serie Fibonacci"""
    lst = []
    a = 0
    b = 1
    counter = 0
    
    while counter < n:
        lst.append(b)
        a,b = b,a+b
        counter += 1
    
    return lst

def fibo_r(n):
    """función recursiva de los n primeros
    números de la serie Fibonacci"""
    
    lst=[]
    
    def _fibo_r(c, pa, pb):
        """clausura que computa los n primeros
        números de la serie Fibonacci"""
        
        if c < n:
            lst.append(pb)
            _fibo_r(c+1,pb,pb+pa)
    
    _fibo_r(0,0,1)    
    return lst

def gen_fibo(n):
    """generador iterativo de los n primeros
    números de la serie Fibonacci"""
    a = 0
    b = 1
    c = 0
    
    while c < n:
        yield b
        a, b = b, b+a
        c += 1
    pass

def gen_fibo_r(n):
    """generador recursivo de los n primeros
    números de la serie Fibonacci"""
    def fibo_r(c, pa, pb):
        if c < n:
            yield pb
            yield from fibo_r(c+1,pb,pa+pb)
            
    yield from fibo_r(0,0,1)
    
print (list(gen_fibo(6)))
print(list(gen_fibo_r(6)))
print(fibo(6))
print(fibo_r(6))