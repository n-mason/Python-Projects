'''
Title: Project 5 Parity

Author: Nathaniel Mason

Credits: N/A
'''
import doctest

def encode(letter):
    '''
    (letter: str) -> str
    Takes a single character string and adds a parity bit to the binary representation of the character.
    Calls: parity

    >>> encode('a')
    '11100001'
    >>> encode('c')
    '01100011'
    >>> encode('f')
    '01100110'
    >>> encode('n')
    '11101110'
    '''
    #calls parity function
    binary_version = bin(ord(letter))
    
    edited_bin_version = binary_version[slice(2, 9)]
    
    parity_bit = parity(edited_bin_version)
    
    final_representation = parity_bit + edited_bin_version 
    
    return final_representation


def parity(bitrep):
    '''
    (bitrep: str) -> str
    Takes a string of 0's and 1's and returns the parity bit, 1 character string

    >>> parity('1100001')
    '1'
    >>> parity('1100110')
    '0'
    >>> parity('1101110')
    '1'
    '''
    #check if sum of the 1-bits in the group is even
    bit_sum = 0
    for i in bitrep:
        bit_sum += int(i)
        
    if bit_sum % 2 == 0:
        return str(0)
    
    else:
        return str(1)

        
def decode(pletter):
    '''
    (pletter: str) -> str
    Takes a string of the binary sequence + parity bit for a character and converts it back to a character in string format.

    >>> decode('11100001')
    'a'
    >>> decode('01100011')
    'c'
    >>> decode('11101000')
    'h'
    '''
    if parity(pletter) == str(0):
        binary_string = pletter[slice(1,8)] #gets rid of parity bit at start of the binary format
        decimal_rep = int(binary_string, base=2)
        character = chr(decimal_rep)
        return character
    
    else:
        return '*'
        
def main():
    '''
    Encodes and decodes the characters in a word by calling functions encode and decode
    '''
    word = 'cat'
    for letter in word:
        print(decode(encode(letter)), end='')
    print()

main()

doctest.testmod()



