#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:42:54 2020

@author: taylorjohnson
"""
import sys
import math



def data(input_file, column):
    """Parses a file based on column selected and stores lines as floats"""
    numbers = []
    non_num = 0
    Count = 0
   
    with open(input_file, 'r') as file:
        for line in file:
            try:        
                column_to_parse = line.split("\t")[column]
                Count = Count + 1
                if column_to_parse == "^[a-zA-Z]+.*":
                    non_num = non_num + 1
                else:
                    numbers.append(float(column_to_parse))
                    for num in numbers:
                        if num != num:
                            numbers.remove(num)
      
            except IndexError:
                sys.exit("There is no valid 'list index' in column {} in line 1 in file: {}".format(column, input_file))
            except ValueError as error:
                print(f"Skipping line number {Count}: could not convert string to float: '{column_to_parse}'")
    
    if numbers == []:
        sys.exit("Error: There were no valid number(s) in column {} in file: {}".format(column, input_file))
    print(f"\nColumn: {column}\n\n\n")
    print("Count\t\t=\t{:9.3f}\n".format(Count), end = '')
    return numbers

def data_ValidNum(numbers):
    """Return ValoidNum for a data set"""
    ValidNum = 0
    for num in numbers:
        ValidNum = ValidNum + 1
    print("ValidNum\t=\t{:9.3f}".format(ValidNum))
    return numbers

def data_average(numbers):
    """Returns the average of a data set"""
    Average = sum(numbers)/len(numbers)
    print("Average\t\t=\t{:9.3f}".format(Average))
    return numbers
    
def data_max(numbers):
    """Returns the maximum number of a data set"""
    Maximum = max(numbers)
    print("Maximum\t\t=\t{:9.3f}".format(Maximum))
    return numbers

def data_min(numbers):
    """Returns the minimum number of a data set"""
    Minimum = min(numbers)
    print("Minimum\t\t=\t{:9.3f}".format(Minimum))
    return numbers

def data_variance(numbers):
    """Returns the variance of a data set"""
    # calculate average
    a = sum(numbers) / len(numbers)
    # calculate variance 
    if len(numbers) == 1:
        Variance = 0
        print("Variance\t=\t{:9.3f}".format(Variance))
    else:
        Variance = sum((i - a) ** 2 for i in numbers) / (len(numbers) - 1)
        print("Variance\t=\t{:9.3f}".format(Variance))
    return numbers

def data_std_dev(numbers):
    """Returns the standard deviation of a data set"""
    # calculate average
    a = sum(numbers) / len(numbers)
    # calculate variance
    if len(numbers) == 1:
        Std_Dev = 0
        print("Std Dev\t\t=\t{:9.3f}".format(Std_Dev))
    else:
        Variance = sum((i - a) ** 2 for i in numbers) / (len(numbers) - 1)
    # calculate standard deviation
        Std_Dev = math.sqrt(Variance)
        print("Std Dev\t\t=\t{:9.3f}".format(Std_Dev))
    return numbers

def data_median(numbers):
    """Returns the median of a data set"""
    numbers.sort()
    medLen = len(numbers) // 2
    Median = (numbers[medLen] + numbers[~medLen]) / 2
    print("Median\t\t=\t{:9.3f}".format(Median))
    return numbers

if __name__ == "__main__":
    # check for two arguments
    arg_count = len(sys.argv) - 1
    if arg_count < 2:
        raise Exception("This function needs two arguments.")
    input_file = sys.argv[1]
    column = int(sys.argv[2])
    numbers = data(input_file, column)
    data_ValidNum(numbers)
    data_average(numbers)
    data_max(numbers)
    data_min(numbers)
    data_variance(numbers)
    data_std_dev(numbers)
    data_median(numbers)

        
        
        

    
    
    
    
