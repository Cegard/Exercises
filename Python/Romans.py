__author__ = "Eduardo Galeano"

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