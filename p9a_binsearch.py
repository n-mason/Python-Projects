'''
Title: Project 9a Binary Search

Author: Nathaniel Mason

Credits: N/A
'''
import doctest

def isMemberI(aseq, target):
    '''
    (aseq: sequence, target: item) -> boolean

    Implements an iterative approach to a binary search algorithm

    >>> isMemberI((1,2,3,3,4), 3)
    True
    >>> isMemberI((), 99)
    False
    '''
    while len(aseq) != 0:
        '''
        if len(aseq) % 2 == 0:
            right_mid_pos = len(aseq) // 2
            left_mid_pos = right_mid_pos - 1
            midpoint = (aseq[left_mid_pos] + aseq[right_mid_pos]) / 2
            print(midpoint)
        '''
        mid_pos = len(aseq) // 2
        midpoint = aseq[mid_pos]
        #print(midpoint)
        
        if midpoint == target:
            return True
        
        elif midpoint > target:
            #print('target less')
            aseq = aseq[:mid_pos] 
            #print(aseq)
            
        elif midpoint < target:
            #print('target more')
            aseq = aseq[mid_pos+1:] #add one because slice operator includes the starting value that we already tested otherwise
            #print(aseq)
            
    if len(aseq) == 0:
        return False
                
                
def isMemberR(aseq, target):
    '''
    (aseq: sequence, target: item) -> boolean

    Implements a recursive approach for a binary search algorithm

    >>> isMemberR((1,2,3,3,4), 6)
    False
    >>> isMemberR(('aeiou'), 'i')
    True
    '''
    if len(aseq) == 0:
        return False
    
    else:
        mid_pos = len(aseq) // 2
        midpoint = aseq[mid_pos]
        #print(midpoint)
        
        if midpoint == target:
            return True
        
        elif midpoint > target:
            #print('target less')
            return isMemberR(aseq[:mid_pos], target) 
            
        elif midpoint < target:
            #print('target more')
            return isMemberR(aseq[mid_pos+1:], target) #add 1 because slice operator includes the starting value that we already tested otherwise
            
def bintest(f):
    '''
    (f: function) -> None

    Implements a set of tests using the function that is defined in the function parameter

    > bintest(isMemberI)
    [returns a list of print statemnts reporting if the returned result value was the expected answer or not]
    '''
    tests = [((1, 2, 3, 3, 4), 3, True), #basic - True
             ((1, 2, 3, 3, 4), 99, False), #basic - False
             ('aeiou', 'i', True), #string sequence - True
             ('aeiou', 'y', False), #string sequence - False
             ((1, 3, 5, 7), 4, False), #even number of items - False
             ((23, 24, 25, 26, 27), 5, False), #odd number of items - False
             ((0, 1, 4, 5, 6, 8), 4, True), #even number of items - True
             ((0, 1, 2, 3, 4, 5, 6), 3, True), #odd number of items - True
             ((1, 3), 1, True), #target is first item - True
             ((2, 10), 10, True), #target is last item - True
             ((99, 100), 101, False), #short sequence - False
             ((42,), 42, True), #one item sequence - True
             ((43,), 44, False), #one item sequence - False
             ((), 99, False)] #empty sequence - False

    
    for i in range(len(tests)):
        (aseq, target, answer) = tests[i]
        result = f(aseq, target)
        
        if result == answer:
            print(f'Checking {f.__name__}({aseq}, {target})...its value {answer} is correct!')
            
        else:
            print(f'Checking {f.__name__}({aseq}, {target})...Error: "{result}", expected "{answer}"')

    return
             
def main():
    '''
    Top level function that calls iterative and recursive binary search functions
    '''
    bintest(isMemberI)
    print()
    bintest(isMemberR)

    return

print(doctest.testmod())
 
if __name__ == '__main__':
    main()
