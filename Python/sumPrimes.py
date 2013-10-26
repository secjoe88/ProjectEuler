# sumPrimes.py
# Author: Joey Willhite
# Date: 10/25/2013


import math
import time
def sumPrimes(maxPrime, dispInc):
# A function to calculate the sum of all of the primes below a given number. Used to solve problem 10
    suspected=3
    primes=[2, suspected]
    primeSum=5
    print('Count:1, Prime Located:2' )
    print('Count:2, Prime Located:3' )
    multiples=dict()

    """initially populate multiples list with multiples of 3"""
    for i in range(3, maxPrime, 3):
        multiples[i]=1
    print('Added multiples of 3 to skip database')


    """Begin method"""
    start=time.clock()
    while suspected<maxPrime:
        suspected +=2
        isComposite=0

        try:
            multiples[suspected]
                
        except KeyError:
            """Otherwise, begin primality testing"""
            for a in primes:
                """Check if suspected prime is divisible by any primes less than or equal to the square root of the
                suspected prim"""
                if a>=math.sqrt(suspected):
                    break
                if suspected%a==0:
                        isComposite=1

            if not (bool(isComposite)):
                """If there are no divisible primes, ad the suspected prime to the prime list, and add to the prime
                sum"""
                primes.append(suspected)
                primeSum+=suspected

                """Also, add any multiples of the newly discovered prime that are less than the maxPrime to the
                multiples dictionary so that they are not checked for primality"""
                temp=2
                while temp*primes[len(primes)-1]<=maxPrime:
                    multiples[temp*primes[len(primes)-1]]=1
                    temp+=1
                """message printing"""
                if len(primes)%dispInc==0:
                    print('Count:' +str(len(primes))+ ', Prime Located:' + str(primes[len(primes)-1]))
                    print('Sum:' + str(primeSum))
                    print('Current Runtime:' +str((time.clock()-start)))
    print()
    print('Last suspected prime:' + str(suspected))
    print('Total runtime:' + str(time.clock()-start))
    print('Total sum:' + str(primeSum))
