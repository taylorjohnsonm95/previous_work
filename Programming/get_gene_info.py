#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 11:28:39 2020

@author: taylorjohnson
"""
# standard and third part imports
import argparse
import sys
import re

# local application imports
from assignment5 import my_io
from assignment5 import config


def main():
    """Returns CLI arguments"""
    args = get_cli_args()
    host, gene = args.HOST.lower(), args.GENE
    file, scientific_name = modify_host_name(host, gene)
    sorted_tissues = get_gene_data(file)
    print_output(scientific_name, gene, sorted_tissues)
    return host, gene


def _print_host_directories():
    """Prints out host names that exist in the directory"""
    print('\nEither the Host Name you are searching for is not in the database\n\n\
or If you are trying to use the scientific name please put the name in \
double quotes:\n\n\
"Scientific name"\n\n\
Here is a (non-case sensitive) list of available Hosts by scientific name\n')
    host_keywords = config.get_host_keywords()
    # remove duplicate values from dictionary
    host_names = list(set(host_keywords.values()))
    # format output so that each host name is numbered
    for index, value in enumerate(host_names, 1):
        print("{:3d}. {}".format(index, value))
    print('\nHere is a (non-case sensitive) list of available Hosts by \
common name\n')
    for index, key in enumerate(host_keywords.keys(), 1):
        print("{:3d}. {}".format(index, key.capitalize()))
    sys.exit()


def modify_host_name(host, gene):
    """Takes a host name and checks if the name is in the directory. \
    If host name does exist, the function will return the scientific name, \
    otherwise the function will alert the directories that do exist."""
    check_name = config.get_host_keywords()
    # search for the host name in the host keyword directory
    scientific_name = check_name.get(host, 0)
    # if the host name is not found, print the directory
    if not scientific_name:
        _print_host_directories()
    else:
        # create a file from the host and gene name
        file = "/".join((config.get_unigene_directory(), \
scientific_name, gene + "." + config.get_unigene_extension()))
        if my_io.is_valid_gene_file_name(file):
            print(f'\nFound Gene {gene} for {scientific_name}')
        else:
            # the gene was not in data and was unable to create a file
            config.get_error_string_4_unable_to_open(file)
            print("Not found")
            print(f'Gene {gene} does not exist for {scientific_name}. \
Exiting now...', file=sys.stderr)
            sys.exit()
    return file, scientific_name


def get_gene_data(file):
    """Extracts a list of tissues in which the gene is expressed and returns \
    a sorted list"""
    tissue_list = []
    gene_file = my_io.get_fh(file, 'r')
    for line in gene_file:
        # find tissue data for the host gene
        if re.search('^EXPRESS', line):
            tissue = line.strip().split('|')
            for element in tissue:
                # remove 'EXPRESS' string from the tissue list
                if element.startswith('EXPRESS'):
                    tissue = element.replace('EXPRESS', '')
                    tissue_list.append(tissue.strip())
                else:
                    tissue_list.append(element.strip())
    # sort the tissues alphabetically
    sorted_tissues = sorted(tissue_list)
    return sorted_tissues


def print_output(scientific_name, gene, sorted_tissues):
    """Prints the tissue expression data"""
    tissue_count = len(sorted_tissues)
    print(f'In {scientific_name}, There are {tissue_count} tissues that {gene} \
is expressed in:\n')
    for index, value in enumerate(sorted_tissues, 1):
        print("{:3d}. {}".format(index, value.capitalize()))


def get_cli_args():
    """
    void: get_cli_args()
    Takes: no arugments
    Returns: instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Give the Host and Gene name')
    parser.add_argument('-host', '--host', dest='HOST', default='Human',
                        type=str, help='Name of Host', required=False)
    parser.add_argument('-gene', '--gene', dest='GENE', default='TGM1',
                        type=str, help='Name of Gene', required=False)
    return parser.parse_args()


if __name__ == "__main__":
    main()
