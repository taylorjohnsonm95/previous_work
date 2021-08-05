#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:42:54 2020

@author: taylorjohnson
"""
import sys
import math



def data(INPUT_FILE, COLUMN):
    """Parses a file based on column selected and stores lines as floats"""
    numbers = []
    non_num = 0
    count = 0
    with open(INPUT_FILE, 'r') as file:
        for line in file:
            try:
                # stores data from column
                column_to_parse = line.split("\t")[COLUMN]
                count = count + 1
                # count non-numbers
                if column_to_parse == "^[a-zA-Z]+.*":
                    non_num = non_num + 1
                else:
                    # append numbers to a list
                    numbers.append(float(column_to_parse))
                    for num in numbers:
                        # remove NaN from numbers list
                        if num != num:
                            numbers.remove(num)
            except IndexError:
                sys.exit("There is no valid 'list index' in column {}\
 in line 1 in file: {}".format(COLUMN, INPUT_FILE))

            except ValueError as error:
                print(f"Skipping line number {count}:\
 could not convert string to float: '{column_to_parse}'")
    # if there are no numbers in the list exit program
    if numbers == []:
        sys.exit("Error: There were no valid number(s)\
 in column {} in file: {}".format(COLUMN, INPUT_FILE))
    print(f"\nColumn: {COLUMN}\n\n\n")
    print("Count\t\t=\t{:9.3f}\n".format(count), end='')
    return numbers


def data_validnum(numbers):
    """Return ValidNum for a data set"""
    validnum = 0
    for num in numbers:
        validnum = validnum + 1
    print("ValidNum\t=\t{:9.3f}".format(validnum))
    return numbers


def data_average(numbers):
    """Returns the average of a data set"""
    average = sum(numbers)/len(numbers)
    print("Average\t\t=\t{:9.3f}".format(average))
    return numbers


def data_max(numbers):
    """Returns the maximum number of a data set"""
    maximum = max(numbers)
    print("Maximum\t\t=\t{:9.3f}".format(maximum))
    return numbers


def data_min(numbers):
    """Returns the minimum number of a data set"""
    minimum = min(numbers)
    print("Minimum\t\t=\t{:9.3f}".format(minimum))
    return numbers


def data_variance(numbers):
    """Returns the variance of a data set"""
    # calculate average
    average = sum(numbers) / len(numbers)
    # calculate variance
    if len(numbers) == 1:
        variance = 0
        print("Variance\t=\t{:9.3f}".format(variance))
    else:
        variance = sum((i - average) ** 2 for i in numbers) / (len(numbers) - 1)
        print("Variance\t=\t{:9.3f}".format(variance))
    return numbers


def data_std_dev(numbers):
    """Returns the standard deviation of a data set"""
    # calculate average
    average = sum(numbers) / len(numbers)
    # calculate variance
    if len(numbers) == 1:
        std_dev = 0
        print("Std Dev\t\t=\t{:9.3f}".format(std_dev))
    else:
        variance = sum((i - average) ** 2 for i in numbers) / (len(numbers) - 1)
    # calculate standard deviation
        std_dev = math.sqrt(variance)
        print("Std Dev\t\t=\t{:9.3f}".format(std_dev))
    return numbers


def data_median(numbers):
    """Returns the median of a data set"""
    numbers.sort()
    med_len = len(numbers) // 2
    median = (numbers[med_len] + numbers[~med_len]) / 2
    print("Median\t\t=\t{:9.3f}".format(median))
    return numbers


if __name__ == "__main__":
    # check for two arguments
    ARG_COUNT = len(sys.argv) - 1
    if ARG_COUNT < 2:
        raise Exception("This function needs two arguments.")
    INPUT_FILE = sys.argv[1]
    COLUMN = int(sys.argv[2])
    NUMBERS = data(INPUT_FILE, COLUMN)
    data_validnum(NUMBERS)
    data_average(NUMBERS)
    data_max(NUMBERS)
    data_min(NUMBERS)
    data_variance(NUMBERS)
    data_std_dev(NUMBERS)
    data_median(NUMBERS)
