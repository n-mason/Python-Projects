'''
Title: Project 7d File Concordance

Author: Nathaniel Mason

Credits: N/A
'''
import string

filename = 'p7dtest.txt'

def fconcordance(fname, case=False):
    '''
    (fname: str, case: boolean) -> Dictionary

    Given a file, fconcordance will return an index of the words in the file, with each line(s) of the file where the word appears.

    >>> fconcordance('p7dtest.txt')
    {'hello': [1, 2], 'world': [1], 'yes': [2], 'test': [3]}
    '''
    
    with open(filename) as f:
        line_number = 0
        line_number_str = ''
        line_number_list = line_number_str.split()
        wordwithcopieslist = []
        wordlist = []
        wordlineDict = {}
        
        for line in f:
            line = line.strip()
            if case == False:
                line = line.lower()
            
        
            for char in line:
                if char in string.punctuation:
                    line = line.replace(char, '')

            wordwithcopieslist.extend(line.split())

        #get rid of copies of words, only unique words will be added to wordlist
        for i in range(len(wordwithcopieslist)):
                if wordwithcopieslist[i] not in wordlist:
                    wordlist.append(wordwithcopieslist[i])

        for item in wordlist:
            wordlineDict[item] = []

        
        f.seek(0) #move pointer back to the top of the file after creating a list of unique words
        for line in f:
            line = line.strip()
            if case == False:
                line = line.lower()
            line_number += 1
            #print(line_number)
            #print(wordlist)
            #print(line)
        
            for item in wordlist:
                if item in line:
                    wordlineDict[item].append(line_number)
                    #print(item)
                    #print(wordlineDict[item])
            
    return wordlineDict


def main():
    '''
    Top level function for file concordance

    Calls: fconcordance
    '''
    #dictionary = fconcordance(filename, case=True)
    dictionary = fconcordance(filename)
    itemList = list(dictionary.keys())
    
    for i in range(len(itemList)):
        print(f"'{itemList[i]}' occurs in lines: {dictionary[itemList[i]]}")

if __name__ == '__main__':
    main()





