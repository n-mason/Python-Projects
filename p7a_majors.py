'''
Title: Project 7-a: Who is in CIS 210?

Author: Nathaniel Mason

Credits: N/A
'''
import doctest
from p6a_data_analysis import frequencyTable

def majors_readf(fname):
    '''
    (fname: string) -> list

    Given a file name, will return the values in that file as a list (not including the
    first two lines in the file)
    
    >>> majors_readf('p7atest.txt')
    ['CIS', 'PHYS', 'DSCI', 'CIS', 'EXPL', 'CIS', 'CIS', 'PHYS', 'PHYS', 'CIS', 'SDSC', 'CIS', 'CIS']

    > majors_readf('majors-short.txt')
    ['CIS', 'SDSC', 'CIS', 'EXPL', 'PBA', 'CIS', 'CIS', 'PHYS', 'DSCI']
    '''
    
    with open(fname) as myfile:
        mystring = myfile.read()
        #print(mystring)
        
        substring = 'CIS 210 Fall 2020\nMajor'
        
        if mystring.startswith(substring):
            majors_string = mystring.replace(substring, '') #gets rid of the header lines in the text file (CIS 210 Fall 2020 and Major in this case)
            #print(majors_string)
            majorsli = majors_string.split()
        else:
            majorsli = mystring.split()
        
        myfile.close()
    
    return majorsli

def majors_analysis(majorsli):
    '''
    (majorsli: list) -> list, int

    Determines the most frequently occurring major(s) in the list and also counts the number of distinct majors in the list

    >>> majors_analysis(['CIS', 'PHYS', 'DSCI', 'CIS', 'EXPL', 'CIS', 'CIS', 'PHYS', 'PHYS', 'CIS', 'SDSC', 'CIS', 'CIS'])
    (['CIS'], 5)
    '''
    aList = majorsli
    
    countDict = {}
    for item in aList:
        if item in countDict:
            countDict[item] += 1
        else:
            countDict[item] = 1

    countList = countDict.values()
    maxCount = max(countList)

    modeList = []
    for item in countDict:
        if countDict[item] == maxCount:
            modeList.append(item)
    #print(countDict)

    majors_mode = modeList  
    majors_ct = len(countDict) #counts number of distinct majors, or in other words number of descriptive words in dictionary
    
    return majors_mode, majors_ct

def majors_report(majors_mode, majors_ct, majorsli):
    '''
    (majors_mode: list, majors_ct: int, majorsli: list) -> None

    Calls: frequencyTable
    
    Reports the mode (or modes if multiple values have highest occurrence), total number of majors represented in the majors list and generates
    a frequency table to report the number of occurrences of each item in majorsli.

    >>> majors_report(['CIS'], 3, ['CIS', 'PHYS', 'EXPL', 'CIS'])
    3 majors are represented in CIS 210 this term.
    The most represented major(s): CIS
    <BLANKLINE>
    ITEM   FREQUENCY
    CIS    2
    EXPL   1
    PHYS   1
    '''
    print(majors_ct,'majors are represented in CIS 210 this term.')

    majors_mode_nicer = majors_mode[0]
    print('The most represented major(s):',majors_mode_nicer)
    print()
    
    majors_table = frequencyTable(majorsli)
    
    return

def main():
    '''
    ()-> None

    Calls: majors_readf, majors_analysis, majors_report

    Top level function for analysis of CIS 210 majors data
    '''
    #fname = 'p7atest.txt'
    fname = 'p7a-majors.txt'

    majorsli = majors_readf(fname) #read
    majors_mode, majors_ct = majors_analysis(majorsli) #analyze
    majors_report(majors_mode, majors_ct, majorsli) #report

    return

if __name__ == '__main__':
    main()

doctest.testmod()



    
