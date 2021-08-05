#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 20:24:54 2020

@author: taylorjohnson
"""
import argparse
import sys
from assignment4 import my_io


def main():
    """Open file"""
    args = get_cli_args()
    infile = args.INFILE
    # opens the infile
    fh_in1 = my_io.get_fh(infile, 'r')
    my_dictionary = gene_description_dictionary(fh_in1)
    input_gene_symbol(my_dictionary)
    return fh_in1


def gene_description_dictionary(fh_in1):
    """parses input file and appends to dictionary"""
    my_dictionary = {}
    for line in fh_in1:
        #parse the first column of the file to get gene names
        gene_name = line.split("\t")[0]
        gene_name = gene_name.lower()
        #parse the second column of the file to get gene descriptions
        description = line.split("\t")[1]
        description = description.lower()
        # add gene names and gene descriptions to dictionary
        my_dictionary[gene_name] = description
    return my_dictionary


def input_gene_symbol(my_dictionary):
    """Asks user to enter gene symbol and prints description"""
    while True:
        gene_symbol = str(input("Enter gene name of interest. Type quit to exit: "))
        gene_symbol_lower = gene_symbol.lower()
        # matches the user input to a gene name in the dictionary
        gene_match = my_dictionary.get(gene_symbol_lower, 0)
        if gene_match:
            #get the description of the gene
            desc = my_dictionary.get(gene_symbol)
            sys.stdout.write(f'{gene_symbol} found! Here is the description:\n{desc}')
        elif not gene_match:
            #exit the loop
            if gene_symbol.lower() == "quit":
                sys.exit(f"Thanks for querying the data.")
            else:
                #continue the loop if no match is found
                sys.stdout.write(f'Not a valid gene name. ')
                continue


def get_cli_args():
    """
    void: get_cli_args()
    Takes: no arugments
    Returns: instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Open chr21_genes.txt, and ask user for a gene name')
    parser.add_argument('-i', '--infile', dest='INFILE',
                        type=str, help='Path to the file to open', required=True)
    return parser.parse_args()

if __name__ == "__main__":
    main()
