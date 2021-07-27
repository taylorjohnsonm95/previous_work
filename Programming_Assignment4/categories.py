#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:39:06 2020

@author: taylorjohnson
"""
import argparse
import collections
from assignment4 import my_io


def main():
    """Open file"""
    args = get_cli_args()
    infile1, infile2 = args.INFILE1, args.INFILE2
    # open infile
    fh_in1 = my_io.get_fh(infile1, 'r')
    # open infile with correct encoding
    fh_in2 = open(infile2, 'r', encoding="ISO-8859-1")
    counts = get_category_count_dictionary(fh_in1)
    descriptions = get_category_description_dictionary(fh_in2)
    combined_list = combine_dictionaries(counts, descriptions)
    write_results(combined_list)
    return fh_in1, fh_in2


def get_category_count_dictionary(infile):
    """Build dictionary containing category and count"""
    categories = []
    # use collections to count occurrence of categories
    counts = collections.defaultdict(int)
    for line in infile:
        if "Category" in line:
            continue
        else:
            #parse the category column
            category = line.split("\t")[2]
            #pass over blank lines
            if category == '\n':
                pass
            else:
                categories.append(category)
    #append category and count to a dictionary
    for category in categories:
        counts[category] += 1
    return counts


def get_category_description_dictionary(infile):
    """Build dictionary containing category and description"""
    descriptions = {}
    for line in infile:
        #parse the category column
        category = line.split("\t")[0]
        #parse the description column
        description = line.split("\t")[1]
        #append categories and descriptions to a dictionary
        descriptions[category] = description
    return descriptions


def combine_dictionaries(dictionary1, dictionary2):
    "Combines two dictionaries after sorting"""
    combined_list = []
    # sort both dictionaries
    sorted_dict1 = dict(sorted(dictionary1.items()))
    sorted_dict2 = dict(sorted(dictionary2.items()))
    # zip dictionaries and create list with categories, counts and descriptions
    for key, value1, value2 in zip(sorted_dict1.keys(), sorted_dict1.values(), sorted_dict2.values()):
        combined = [key, value1, value2]
        combined_list.append(combined)
    return combined_list


def write_results(combined_list):
    """Writes results to a new file"""
    #create output path
    output = 'OUTPUT/categories.txt'
    #open output file
    out_file = my_io.get_fh(output, 'w')
    #write headers to file
    out_file.write(f'Category\tOccurrence\tDescription\n')
    #write lists to file
    for _list in combined_list:
        out_file.write(f'{_list[0]}\t{_list[1]}\t{_list[2]}')

def get_cli_args():
    """
    void: get_cli_args()
    Takes: no arugments
    Returns: instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Combine on gene name and count the category occurrence')
    parser.add_argument('-i1', '--infile1', dest='INFILE1',
                        type=str, help='Path to the gene description file to open', required=True)
    parser.add_argument('-i2', '--infile2', dest='INFILE2',
                        type=str, help='Path to the gene category to open', required=True)
    return parser.parse_args()


if __name__ == "__main__":
    main()
