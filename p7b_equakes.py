'''
Title: Project 7b Earthquake Data

Author: Nathaniel Mason

Credits: N/A
'''

import doctest
import p6a_data_analysis

def equake_readf(fname):
    '''
    (fname: str) -> list

    Reads the earthquake data from a file and returns a list of the earthquake magnitudes

    >>> equake_readf('p7b-equakes25ftest.csv')
    [2.56, 3.17, 2.55, 3.08, 2.8]
    '''
    with open(fname) as f:
        f.readline() #skip header
        magnitudes = []
        
        for line in f:
            equake_vals = line.strip().split(',')
            
            magnitudes.append(float(equake_vals[4]))
        
    return magnitudes

def equake_analysis(magnitudes):
    '''
    (magnitudes: list) -> float, float, list

    Takes the list of earthquake magnitudes and returns the mean, median and mode(s)

    >>> equake_analysis([2.56, 3.17, 2.55, 3.08, 2.8])
    (2.832, 2.8, [2.56, 3.17, 2.55, 3.08, 2.8])
    '''
    meanmag = p6a_data_analysis.mean(magnitudes)
    medianmag = p6a_data_analysis.median(magnitudes)
    modemag = p6a_data_analysis.mode(magnitudes)
    
    return meanmag, medianmag, modemag

def equake_report(magnitudes, mmm, minmag):
    '''
    (magnitudes: list, mmm: tuple, minmag: float) -> None

    Takes the list of magnitudes, the mean, median, mode and minimum magnitude and reports them to the user

    >>> equake_report([2.56, 3.17, 2.55, 3.08, 2.8], (2.832, 2.8, [2.56, 3.17, 2.55, 3.08, 2.8]), 2.5)
    There have been 5 earthquakes with magnitude 2.5 or higher over the past 100 years.
    <BLANKLINE>
    Mean magnitude is: 2.832
    Median magnitude is: 2.8
    Mode(s) of magnitudes is: [2.56, 3.17, 2.55, 3.08, 2.8]
    <BLANKLINE>
    ITEM   FREQUENCY
    2.55   1
    2.56   1
    2.8    1
    3.08   1
    3.17   1
    '''
    mag_count = len(magnitudes)
    print('There have been',mag_count,'earthquakes with magnitude', minmag, 'or higher over the past 100 years.')
    print()
    print('Mean magnitude is:', mmm[0])
    print('Median magnitude is:', mmm[1])
    print('Mode(s) of magnitudes is:', mmm[2])
    print()
    p6a_data_analysis.frequencyTable(magnitudes) #generates a table with the number of occurrences of each item in magnitudes
    
    return 

def main():
    '''
    () -> None

    Calls: equake_readf, equake_analysis, equake_report

    Top level function for earthquake data analysis
    '''
    #fname = 'p7b-equakes25f.csv'
    #minmag = 2.5
    fname = 'p7b-equakes50f.csv'
    minmag = 5.0

    emags = equake_readf(fname)
    mmm = equake_analysis(emags)
    equake_report(emags, mmm, minmag)

if __name__ == '__main__':
    main()

doctest.testmod()


    
