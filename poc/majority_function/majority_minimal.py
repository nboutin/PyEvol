'''
Created on 12 juil. 2019

@author: nboutin
'''

def majorityFunction(a,b,c):
    '''M(A,B,C)=AB+AC+BC'''
    return a and b or a and c or b and c

