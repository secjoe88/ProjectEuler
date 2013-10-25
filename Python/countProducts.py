# countProducts.py
# Author: Joey Willhite
# Date: 10/24/2013


def countProducts(digits, numfactors):
# A simple method to count the products of successive digits in a number. The input value 'digits' is a
# string containing the number, and 'numfactors' is the number of digits to multiply. Used to solve 
# problem #8
    greatestProduct=0
    currentProduct=0
    for i in range(len(digits)-(numfactors-1)):
        currentProduct=int(digits[i])
        for j in range(numfactors-1):
            currentProduct=currentProduct*int(digits[i+j+1])
        print('current product:' + str(currentProduct))
        if currentProduct>greatestProduct:
            greatestProduct=currentProduct
        currentProduct=0
    return greatestProduct
