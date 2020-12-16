'''
Title: Project 3a - UO Dash 

Author: Nathaniel Mason

Credits: N/A
'''
from turtle import *
from random import randint
from time import sleep

def jump(x, y):
    '''(x: number, y: number) 

    move turtle without leaving a track to position (x,y).
    like turtle setpos but pen is always up for the move
    and put down after

    >>> jump(0,0)
    [return turtle to center]
    '''
    pu()
    setpos(x,y)
    pd()

    return

def uo_dash():
    '''
    turtle will dash from 18th ave entrance to 13th ave
    will it run a personal best?  report time (steps).
    
    >>> uo_dash()
    '''
    FINISH_LINE = 32
    
    # set the scene
    reset()
    clear()
    title('CIS Dash')
    pencolor('purple')
    pensize(3)
    bgpic('uo_campus_map.png')
    screensize(1195, 681)

    jump(-110, -312)
    stamp() #mark start of route at University and 18th
    write('START', align ='center', font=('Arial', 10, 'bold'))

    jump(-110, 43)
    write('FINISH', align ='center', font=('Arial', 10, 'bold'))

    jump(-110, -325)
    lt(90)
    shape('turtle')
    color('green')    
    speed(randint(0, 10))

    print('ON YOUR MARK, GET SET')
    sleep(3)       # WHAT IS THIS? Use Python help function to check.
    print('GO')

    # race to the finish
    count = 0
    
    while pos() <= (-110,FINISH_LINE):
        fd(randint(1,5)) #move the turtle one step that is between 1 and 5 units long 
        count += 1 #add 1 to the step count
        
    # report time (steps)
    print('It took the turtle',count,'steps to get to the finish line and finish the race!')
          
    return 
    
uo_dash()
