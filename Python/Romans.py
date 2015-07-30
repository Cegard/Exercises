__author__ = "Eduardo Galeano"
'''
def parse_to_roman(n):
    """gives the roman representation of the given number
    :param n: the decimal number to be parsed
    :returns: roman representation"""
    
    number = ''
    
    def add_substract(chars, unit):
        
        nonlocal number, n
        
        """adds the chars to the roman representation
        while substracts to the number.
        :param chars: the chars to be added
        :param unit: the units to be substracted"""
        
        while n >= unit:
            n -= unit
            number += chars
    
    add_substract('M', 1000)
    
    add_substract('CM', 900)
    
    add_substract('D', 500)
    
    add_substract('CD', 400)
    
    add_substract('C', 100)
    
    add_substract('XC', 90)
    
    add_substract('L', 50)
    
    add_substract('XL', 40)
    
    add_substract('X', 10)
    
    add_substract('IX', 9)
    
    add_substract('V', 5)
    
    add_substract('IV', 4)
    
    add_substract('I', 1)
    
    
    return number
'''

def parse_to_roman(n):
    number = ''
    
    number += 'M'*(n//1000) if n >= 1000 else ''
    n -= 1000*(n//1000)
    
    number += 'CM'*(n//900) if n >= 900 else ''
    n -= 900*(n//900)
    
    number += 'D'*(n//500) if n >= 500 else ''
    n -= 500*(n//500)
    
    number += 'CD'*(n//400) if n >= 400 else ''
    n -= 400*(n//400)
    
    number += 'C'*(n//100) if n >= 100 else ''
    n -= 100*(n//100)
    
    number += 'XC'*(n//90) if n >= 90 else ''
    n -= 90*(n//90)
    
    number += 'L'*(n//50) if n >= 50 else ''
    n -= 50*(n//50)
    
    number += 'XL'*(n//40) if n >= 40 else ''
    n -= 40*(n//40)
    
    number += 'X'*(n//10) if n >= 10 else ''
    n -= 10*(n//10)
    
    number += 'IX'*(n//9) if n >= 9 else ''
    n -= 9*(n//9)
    
    number += 'V'*(n//5) if n >= 5 else ''
    n -= 5*(n//5)
    
    number += 'IV'*(n//4) if n >= 4 else ''
    n -= 4*(n//4)
    
    number += 'I'*(n//1) if n >= 1 else ''
    n -= 1*(n//1)
    
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