__author__ = "Eduardo Galeano"

def parse_to_roman(n):
    """gives the roman representation of the given number
    :param n: the decimal number to be parsed
    :returns: roman representation"""
    
    number = ''
    
    while n >= 1000:
        n -= 1000
        number += 'M'
    
    while n >= 900:
        n -= 900
        number += 'CM'
    
    while n >= 500:
        n -= 500
        number += 'D'
    
    while n >= 400:
        n -= 400
        number += 'CD'
    
    while n >= 100:
        n -= 100
        number += 'C'
    
    while n >= 90:
        n -= 90
        number += 'XC'
    
    while n >= 50:
        n -= 50
        number += 'L'
    
    while n >= 40:
        n -= 40
        number += 'XL'
    
    while n >= 10:
        n -= 10
        number += 'X'
    
    while n >= 9:
        n -= 9
        number += 'IX'
    
    while n >= 5:
        n -= 5
        number += 'V'
    
    while n >= 4:
        n -= 4
        number += 'IV'
    
    while n >= 1:
        n -= 1
        number += 'I'
    
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