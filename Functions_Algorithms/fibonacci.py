#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 10:14:30 2020

@author: taylorjohnson
"""
import sys

def population(n, k):
    """Computes the population size"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    if n > 10000:
        sys.exit()
    elif k > 10000:
        sys.exit()
    
    population = [0] * n
    population[0] = 1
    population[1] = 1

    for i in range(2, n):
        offspring = population[i-2] * k
        population[i] = population[i-1] + offspring
        
    return population[n-1]
        
        
        
if __name__ == "__main__":
    #check for two arguments
    arg_count = len(sys.argv) - 1
    if arg_count < 2:
        raise Exception("This requires 2 arguments.")
    else:
        n = int(sys.argv[1])
        k = int(sys.argv[2])
        total = population(n, k)
        print(total)





       
