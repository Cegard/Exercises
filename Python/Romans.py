__author__ = "Eduardo Galeano"

def parse_to_roman(n):
    number = ''
    
    def _add_substract(unit, char):
        nonlocal number, n
        
        number += char*(n//unit) if n >= unit else ''
        n -= unit*(n//unit)
    
    _add_substract(1000, 'M')
    
    _add_substract(900, 'CM')
    
    _add_substract(500, 'D')
    
    _add_substract(400, 'CD')
    
    _add_substract(100, 'C')
    
    _add_substract(90, 'XC')
    
    _add_substract(50, 'L')
    
    _add_substract(40, 'XL')
    
    _add_substract(10, 'X')
    
    _add_substract(9, 'IX')
    
    _add_substract(5, 'V')
    
    _add_substract(4, 'IV')
    
    _add_substract(1, 'I')
    
    return number

#number = input()

n0 = 8
n1 = 991
n2 = 1523
n3 = 1024
n4 = 3589

print(n0, ' en romanos es: ', parse_to_roman(n0))
print(n1, ' en romanos es: ', parse_to_roman(n1))
print(n2, ' en romanos es: ', parse_to_roman(n2))
print(n3, ' en romanos es: ', parse_to_roman(n3))
print(n4, ' en romanos es: ', parse_to_roman(n4))