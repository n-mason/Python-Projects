'''
Title: Project 6c, Zip to Bar Code

Author: Nathaniel Mason

Credits: N/A
'''

import doctest

from turtle import *

def checkDigit(zipcode):
    '''
    (zipcode: int) -> int

    Returns the check digit for a given zipcode

    >>> checkDigit(97403)
    7
    >>> checkDigit(23443)
    4
    >>> checkDigit(45010)
    0
    >>> checkDigit(00000)
    0
    '''
    digit_sum = 0

    #add up the digits of the zipcode
    while zipcode != 0:
        digit = zipcode % 10
        zipcode = zipcode // 10
        digit_sum += digit

    #find the remainder of the sum / 10
    sum_remainder = digit_sum % 10

    #subtract remainder from 10 to obtain check digit unless remainder is 0
    if sum_remainder == 0:
        check_digit = 0
    else:
        check_digit = 10 - sum_remainder

    return check_digit


def zipToBinList(zipcode):
    '''
    (zipcode: int) -> str
    
    Returns a binary list by taking the given zipcode, adding the check_digit and then converting to binary

    >>> zipToBinList(97403)
    '101001000101001110000011010001'
    '''
    check_digit = checkDigit(zipcode)
    zip_and_check_code_str = str(zipcode) + str(check_digit)
    binary_list = ''
    for i in zip_and_check_code_str:
        if i == '0':
            binary_list += '11000'
        elif i == '1':
            binary_list += '00011'
        elif i == '2':
            binary_list += '00101'
        elif i == '3':
            binary_list += '00110'
        elif i == '4':
            binary_list += '01001'
        elif i == '5':
            binary_list += '01010'
        elif i == '6':
            binary_list += '01100'
        elif i == '7':
            binary_list += '10001'
        elif i == '8':
            binary_list += '10010'
        elif i == '9':
            binary_list += '10100'
    
    return binary_list


def zipToBar(zipcode):
    '''
    (zipcode: int) -> bars drawn in Turtle

    Draws the barcode in turtle graphics based on a zipcode. Guard rails are drawn, as well as the zipcode
    and check digit in bar form
    '''
    reset()
    speed(9)
    bin_list = zipToBinList(zipcode)
    pu()
    setpos(-350,0)
    
    #guard rail 1
    lt(90)
    pd()
    fd(100)
    pu()
    bk(100)
    rt(90)
    fd(20) 

    #zipcode and check digit in bar form     
    for i in bin_list:
        if i == '0':
            lt(90)
            pd()
            fd(50)
            pu()
            bk(50)
            rt(90)
            fd(20)
        elif i == '1':
            lt(90)
            pd()
            fd(100)
            pu()
            bk(100)
            rt(90)
            fd(20)
    
    #guard rail 2
    lt(90)
    pd()
    fd(100)
    pu()
    bk(100)
    rt(90)
    fd(20) 
    
def main():
    prompt = input('Enter a zip code value: ')
    zipcode = int(prompt)
    zipToBar(zipcode)

main()

doctest.testmod()
