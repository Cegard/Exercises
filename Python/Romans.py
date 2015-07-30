__author__ = "Eduardo Galeano"


def parse_to_roman(m):
    """gives the roman representation of the given number
    :param m: the decimal number to be parsed
    :returns: roman representation"""
    
    # lista de tuplas cada una contiene la cifra decimal y su respectiva representación en romanos
    numbers = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
        (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    
    def _parse(n, tuples):
        """gives the representation of the given number, according to the given list
        :param n: the decimal number to be parsed
        :returns: the number parsed"""
        
        number = ''
        
        def _add_substract(unit, char):
            """adds the chars to the representation
            while substracts to the number.
            :param chars: the chars to be added
            :param unit: the units to be substracted"""
            
            nonlocal number, n
            
            number += char*(n//unit) if n >= unit else ''
            n -= unit*(n//unit)
        
        for t in tuples: _add_substract(t[0],t[1])
        
        return number
    
    return _parse(m, numbers)


err_msg = 'número ingeresado no valido'
print("por favor digite el número a pasar a romanos que no sea mayor a 4000")

number = input()

try:
    number = int(number)
    if number < 4000 and number > 0: print(number, ' en romanos es: ', parse_to_roman(number))
    else: print(err_msg)
except:
    print(err_msg)