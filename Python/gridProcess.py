# gridProcess.py
# Author: Joey Willhite
# Date: 11/13/2013


def gridProcess(file_name):
# A function to find the product of any horizontal, vertical, or diagonal group of 4 numbers in a 20x20 grid. Used
# to solve problem #11
    file=open(file_name, 'r')
    matrix=[[0 for i in range(20)] for j in range(20)]
    max=0

    """Read in values from file and parse as values are read"""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            """Read value, place in matrix"""
            matrix[i][j]=int(file.read(2))
            file.read(1)
            """Check horizontal and left diagonal products (if there are sufficient matrix entries)"""
            if j+1>=4:
                temp=calcHorizProduct(matrix,i,j)
                if temp>max:
                    print('Old max:' + str(max) + ' new max:' + str(temp))
                    max=temp
                if i+1>=4:
                    temp=calcLeftDiagProd(matrix, i, j)
                    if temp>max:
                        print('Old max:' + str(max) + ' new max:' + str(temp))
                        max=temp

            """Check right diagonal products and vertical products (if there are sufficient matrix entries)"""
            if i+1>=4:
                temp=calcVertProduct(matrix,i,j)
                if temp>max:
                    print('Old max:' + str(max) + ' new max:' + str(temp))
                    max=temp
                if (j+1)<=17:
                    temp=calcRightDiagProd(matrix, i, j)
                if temp>max:
                    print('Old max:' + str(max) + ' new max:' + str(temp))
                    max=temp
                
                

    print('Global max is:' + str(max))

"""Helper methods to calculate various products"""    
def calcVertProduct(matrix,i,j):
    currentMax=matrix[i][j]*matrix[i-1][j]*matrix[i-2][j]*matrix[i-3][j]
    return currentMax

def calcHorizProduct(matrix,i,j):
    currentMax=matrix[i][j]*matrix[i][j-1]*matrix[i][j-2]*matrix[i][j-3]
    #print('Current left horizontal product:' + str(currentMax))
    return currentMax

def calcLeftDiagProd(matrix, i, j):
    currentMax=matrix[i][j]*matrix[i-1][j-1]*matrix[i-2][j-2]*matrix[i-3][j-3]
    #print ('I:'+str(i+1)+', J:'+str(j+1)+' Left diagonal product:' +str(currentMax))
    return currentMax

def calcRightDiagProd(matrix, i, j):
    currentMax=matrix[i][j]*matrix[i-1][j+1]*matrix[i-2][j+2]*matrix[i-3][j+3]
    #print ('I:' +str(i+1)+', J:'+str(j+1)+', Right diagonal product:' +str(currentMax))
    return currentMax
