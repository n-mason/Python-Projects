'''
Title: Project 3b - FizzBuzz

Author: Nathaniel Mason

Credits: N/A
'''
def fb(n):
    '''
    (n: int)->str

    returns fizz, buzz, fizzbuzz or the current number i depending on if the number is a multiple of the specificed checks
    (in this case, multiple of 3=fizz, mult of 5=buzz, mult of 3 and 5=fizzbuzz)

    >>> fb(5)
    1
    2
    fizz
    4
    buzz
    '''
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0: #if the number is a multiple of 3 and 5 print fizzbuzz
            print('fizzbuzz')
        elif i % 3 == 0: #if the number is a multiple of 3 print fizz
            print('fizz')
        elif i % 5 == 0: #if the number is a multiple of 5 print buzz
            print('buzz')
        else:
            print(i) #otherwise print the number

    return

def main():
    '''
    asks for a number and calls the fb function using that number

    calls: fb

    >>> main()
    '''
    number_prompt = input("Enter a number that will end the fizzbuzz game: ")
    number_input = int(number_prompt)
    fb(number_input)

main() 




#2nd Method for FizzBuzz

def alt_fb(n):
    '''
    (n: int)->str

    returns a string named output after concatenating any appropriate numbers that work as multiples
    (in this case, multiple of 3 adds fizz to ouput string, mult 5 adds buzz, mult 7 adds fuzz)

    >>> alt_fb(7)
    1
    2
    fizz
    4
    buzz
    fizz
    fuzz
    '''
    
    #this code works better if want to check other numbers...
    for i in range(1, n+1):
        output = ''
        if i % 3 == 0: #if the number is a multiple of 3 concatenate fizz to output string
            output += 'fizz'
        if i % 5 == 0: #if the number is a multiple of 5 concatenate buzz to output string
            output += 'buzz'
        if i % 7 == 0: #if the number is a multiple of 7 concatenate fuzz to output string
            output += 'fuzz'
        if output == '': #if the output string is still empty after all checks, assign the output to the current number i
            output = i
            
        print(output)

def main_2():
    '''
    asks for a number and calls the alt_fb function using that number

    calls: fb

    >>> main_2()
    '''
    number_prompt = input("Enter a number that will end the fizzbuzz game: ")
    number_input = int(number_prompt)
    alt_fb(number_input)

#main_2()
        

