#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:04:24 2020

@author: taylorjohnson
"""
import sys
 
    
def get_fh(file_name, mode):
    """Open a file for reading or writing"""
    try:
        fh_in = open(file_name, mode)
    except IOError:
        print(f"The file {file_name} could not be opened.")
        sys.exit(1)
    except ValueError:
        print(f"The wrong argument {mode} was passed for opening mode.")
        sys.exit(1)
    return fh_in


def _check_size_of_lists(list1, list2):
    """Helper function of get_header_and_seq_lists"""
    if len(list1) != len(list2):
        print("Error: Lists have unequal sizes.")
        sys.exit(1)
    return True


def get_header_and_seq_lists(fh_in):
    """Returns header and sequence lists"""
    list_headers = []
    list_seqs = []
    sequences = ''
    for line in fh_in:
        if ">" in line:
            list_headers.append(line.strip())
            if sequences != '':
                list_seqs.append(sequences)
            sequences = ''
        else:
            sequences += line.strip()
    list_seqs.append(sequences.strip())
    # call helper function to chek=ck list size
    check_list = _check_size_of_lists(list_headers, list_seqs)
    return list_headers, list_seqs