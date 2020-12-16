'''
Title: Project 2-b - Art Show 

Author: Nathaniel Mason

Credits: 
'''
from turtle import *

def jump(x, y):
    '''
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


def square(side_len, scolor=''):
    '''
    (side_len: float, scolor: str) -> shape in turtle)
    draw a square with a black outline that has sides of size "side_len" and color determined by "scolor"

    >>> square(30,'blue')
    [draw a blue square with sides of length 30]
    '''
    pencolor('black')
    fillcolor(scolor)
    begin_fill()    
    for x in range(4):
        fd(side_len)
        rt(90)
    end_fill()    

    return


def triangle(side_len, scolor=''):
    '''
    draw an equilateral triangle with sides of size "side_len" and color determined by "scolor"

    >>> triangle(60,'purple')
    [draw a purple triangle with sides of length 60]
    '''
    fillcolor(scolor)
    begin_fill()   
    for x in range(3):
        fd(side_len)
        lt(120)
    end_fill()     
    
    return


def poly(num_sides, side_len, pcolor=''):
    '''
    (num_sides: int, side_len: float, pcolor: str) -> shape drawn in turtle
    
    draw a polygon of color "pcolor" with a number of sides defined by "num_sides" with each length having a size of "side_len"

    >>> poly(8, 50, 'red')
    [draw a red octagon with sides of length 50]
    '''
    fillcolor(pcolor)
    begin_fill()
    for x in range(num_sides):
        fd(side_len)
        lt(360/num_sides)
    end_fill()

    return


def house():
    '''
    draw a square and a triangle to form a house along with a second square to make a door

    calls: poly
    
    >>> house()
    '''
    house_side = poly(4,100,'lightblue') #draws the main square part of the house and fills it lightblue
    jump(0,100)
    poly(3,100,'black') #draws the roof and fills it black
    jump(36,0)
    door_side = poly(4,28,'brown') #draws the small square door and fills it brown

    return


def flower():
    '''
    draw a green stem and flower petals to the left of the house

    calls: poly

    >>> flower()
    '''
    jump(-20,0)
    pencolor('green')
    fillcolor('green')
    
    #drawing the stem
    pensize(2) #defines how thickly the stem will be drawn (thin in this case)
    begin_fill()   
    fd(2)
    lt(90)
    fd(40)
    lt(90)
    fd(2)
    lt(90)
    fd(40)
    end_fill()     
    
    #drawing the petals
    jump(-20,40)
    pencolor('black')
    pensize(1) #makes the petal outlines thin
    begin_fill()    
    for x in range(12): #repeats the triangle and the rotation 12 times
        poly(3,10,'violet') #draws a violet triangle with sides of length 10
        lt(40)
    end_fill()   
        
    return


def sunshine():
    '''
    draw a sun in the upper right with rays of length 150 that rotate around a point

    >>> sunshine()
    '''
    jump(300,300)
    pensize(5) #make the rays relatively thick
    pencolor('yellow')
    for x in range(36):
        fd(150)
        bk(150)
        lt(10)

    return


def art_show_main():
    '''
    draw a picture of a house and sun and flower
    
    calls: house, flower, sunshine

    >>> art_show_main()
    '''
    reset()
    clear() 
    title("A Sunny Day")
    speed('fastest')
    hideturtle()
    
    house()       
    flower()
    sunshine()

    return 

