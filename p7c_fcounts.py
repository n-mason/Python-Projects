'''
Title: Project 7c Inspecting Files

Author: Nathaniel Mason

Credits: N/A
'''
import doctest
import string

def fcounts(fname, case=False):
    '''
    (fname: str) -> int, int, int, int, frequency table printed

    Given a file name, will return the line count, word count, character count with spaces and without spaces
    and a dictionary with the number of occurrences of each word in the file.

    >>> fcounts('p7ctest.txt')
    (2, 4, 21, 23, {'hello': 2, 'world': 1, 'yes': 1})
    '''
    with open(fname) as f:
        linecount = 0
        wordlist = []
        charcountnospaces = 0
        charcountwithspaces = 0
        wordsstringnospaces = ''
        
        for line in f:
            if case == False:
                line = line.lower()
            linecount += 1
            line = line.strip()
            
            for char in line:
                charcountwithspaces += 1
                if char != ' ':
                    wordsstringnospaces += char
                if char in string.punctuation:
                    line = line.replace(char, '')
                    
            wordlist.extend(line.split())

        wordcount = len(wordlist)
        charcountnospaces = len(wordsstringnospaces)
        

    #Generate a dictionary with the number of occurrences of each word in the file
        countDict = {}

        for item in wordlist:
            if item in countDict:
                countDict[item] = countDict[item] + 1
            else:
                countDict[item] = 1
    
    return linecount, wordcount, charcountnospaces, charcountwithspaces, countDict

def main():
    '''
    () -> None

    Calls: fcounts

    Top level function for getting data about text file
    '''
    filename = 'p7ctest.txt'
    fcounts_data = []
    '''
    #Test with case enabled
    fcounts_data.extend(fcounts(filename, case=True))
    '''
    fcounts_data.extend(fcounts(filename))
    #print(fcounts_data)
    
    print(f'In file {filename}:')
    print('The number of lines is:', fcounts_data[0])
    print('The number of words is:', fcounts_data[1])
    print('The number of characters (no spaces) is:', fcounts_data[2])
    print('The number of characters (with spaces) is:', fcounts_data[3])
    print()
    print(f'Word occurrences in file {filename}:')
    print("ITEM", "  FREQUENCY") 

    countDict = fcounts_data[4]
    itemList = list(countDict.keys())
    #print(countDict.keys())
    #print(itemList)
    itemList.sort()
    for item in itemList:
        print(f'{item:<7}{countDict[item]}') #align the items and frequency to the left, space not
                                             #dependent on item word length anymore
        
    return

doctest.testmod()
    
if __name__ == '__main__':
    main()

