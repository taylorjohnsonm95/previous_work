#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 10:57:28 2020

@author: taylorjohnson
"""
import argparse
import sys
from assignment4 import my_io


def main():
    """Opens files"""
    args = get_cli_args()
    infile1, infile2 = args.INFILE1, args.INFILE2
    # open input file1
    fh_in1 = my_io.get_fh(infile1, 'r')
    # open input file 2
    fh_in2 = my_io.get_fh(infile2, 'r')
    intersection = get_intersection(fh_in1, fh_in2)
    write_results(intersection)
    return fh_in1, fh_in2
    fh_in1.close()
    fh_in2.close()

def get_intersection(infile1, infile2):
    """Gets the intersection of two lists"""
    list1 = []
    list2 = []
    for line in infile1:
        #split line to append gene from first column for file 1
        line = line.split("\t")
        line = [x.strip() for x in line]
        list1.append(line[0])
    del list1[0]
    for line in infile2:
        #split line to append gene from first column for file 2
        line = line.split("\t")
        line = [x.strip() for x in line]
        list2.append(line[0])
    # delete the header
    del list2[0]
    # finds the genes that match from both files
    intersection = set(list1).intersection(set(list2))
    # count of matching genes
    intersection_count = len(intersection)
    # count of genes in file 1
    unique_count_list1 = len(set(list1))
    # count of genes in file 2
    unique_count_list2 = len(set(list2))
    sys.stdout.write(f'Number of unique gene names in {infile1.name}: {unique_count_list1}\n\
Number of unique gene names in {infile2.name}: {unique_count_list2}\n\
Number of common gene symbols found: {intersection_count}\n\
Output stored in OUTPUT/intersection_output.txt')
    return intersection


def write_results(intersection):
    """Writes results to file"""
    # create path to write results
    output = 'OUTPUT/intersection_output.txt'
    # open file to write results
    out_file = my_io.get_fh(output, 'w')
    # sort genes alphabetically
    intersection_sorted = sorted(intersection)
    # add newline character between each gene
    out_genes = "\n".join(intersection_sorted)
    #write to file
    out_file.write(out_genes)


def get_cli_args():
    """
    void: get_cli_args()
    Takes: no arugments
    Returns: instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Provide two gene list \
(ignore header line), find intersection')
    parser.add_argument('-i1', '--infile1', dest='INFILE1',
                        type=str, help='Gene list 1 to open', required=True)
    parser.add_argument('-i2', '--infile2', dest='INFILE2',
                        type=str, help='Gene list 2 to open', required=True)
    return parser.parse_args()


if __name__ == "__main__":
    main()
