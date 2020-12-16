'''
Title: Project 2-b - Python Variations

Author: Nathaniel Mason

Credits: N/A
'''
def add_digits(n):
    '''
    return the sum of the digits of a 3-digit integer number

    >>> add_digits(456)
    [returns 15]
    '''
    ones_digit = n%10
    tens_digit = (n%100)//10 #gets the remainder and then uses floor division to get tens place
    hundreds_digit = n//100

    result = ones_digit + tens_digit + hundreds_digit
    
    print("The sum of the giits in", n, "is", result)
          
    return 


def profit(attendees):
    '''
    return the net profit per show given the number of attendees at the show

    >>> profit(10)
    [returns 25.0]
    '''
    ticket_revenue = attendees * 5 #theatre makes 5$ per attendee
    show_cost = 20 #theatre must pay 20$ to put on the show
    attendee_cost = attendees*0.5 #each attendee adds $0.50 to the cost

    net_profit = ticket_revenue - (show_cost + attendee_cost)
    final_answer = round(net_profit, 2)
    
    return final_answer


def profit_main():
    '''
    return the net profit for a number of examples defined below

    calls: profit

    >>>profit_main()
    '''
    #call profit ten times and report results
    print("Profit for 5 customers would be: $", profit(5))
    print("Profit for 10 customers would be: $", profit(10))
    print("Profit for 15 customers would be: $", profit(15))
    print("Profit for 20 customers would be: $", profit(20))
    print("Profit for 25 customers would be: $", profit(25))
    print("Profit for 30 customers would be: $", profit(30))
    print("Profit for 35 customers would be: $", profit(35))
    print("Profit for 40 customers would be: $", profit(40))
    print("Profit for 45 customers would be: $", profit(45))
    print("Profit for 50 customers would be: $", profit(50))

    return


def gravity(v):
    '''
    return the time it will take for a parcel thrown from an airplane at v meters per second to hit the ground

    >>>gravity(1)
    [returns 47.28 seconds]
    '''
    import math

    v = float(v)
    t = (v - math.sqrt((v**2) - (4 * (-4.9) * 11000))) / (2 * (-4.9)) #provides the time required
    t = float(t)
    dist_from_ground = (-4.9 * (t**2)) - (v * t) + 11000 #quadratic equation for the distance from the ground
    final_time = round(t,2)

    print("Time to ground from 11000 meters for",v,"m/sec is",final_time,"seconds.")
    
    return 

#Challenge
def end_time(h,m,d):
    '''
    Given the starting time and lenght of an event, print the ending time of the event

    >>> end_time(23, 59, 7)
    [returns 0 : 6 o'clock as the end time]
    '''
    overall_mins = m + (h * 60)
    end_minutes = (overall_mins+d) % 60
    end_hour = ((overall_mins+d) // 60) % 24
    
    print("End time is", end_hour, ":", end_minutes, "o'clock")






    


