# generateTriplets.py
# Author: Joey Willhite
# Date: 10/25/2013

import math
def generateTriplets(sum):
# A function that generates pythagorean triplets until there is one whose sum matches the inputed sum.
# Used to solve problem #9 
    a, b, c=0, 1, 0
    while a<=333:
        a+=1
        b=a
        c=0
        while a+b+c<=sum:
            b+=1
            c=math.sqrt(math.pow(a,2)+math.pow(b,2))
            if c%1==0:
                print('Triplet found: (' +str(a)+',' +str(b)+','+str(c)+')')
            if a+b+c==sum:
                print('Desired Sum Found')
                return(str(a)+','+str(b)+','+str(c))
    return 'Desired sum not found.'
