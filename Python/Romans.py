__author__ = "Eduardo Galeano"

def parse_to_roman(n):
    """gives the roman representation of the given number
    :param n: the decimal number to be parsed
    :returns: roman representation"""
    
    # lista de tuplas cada una contiene la cifra decimal y su respectiva representación en romanos
    numbers = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
        (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (4, 'I')]
    
    number = ''
    
    def _add_substract(unit, char):
        """adds the chars to the roman representation
        while substracts to the number.
        :param chars: the chars to be added
        :param unit: the units to be substracted"""
        
        nonlocal number, n
        
        number += char*(n//unit) if n >= unit else ''
        n -= unit*(n//unit)
    
    for t in numbers: _add_substract(t[0],t[1])
    
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