#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:48:24 2020

@author: taylorjohnson
"""

import sys
import argparse

def main():
    """ read and parse input file to write to ouput file"""
    args = get_cli_args()
    file_name = args.INFILE
    # read input file
    fh_in = get_fh(file_name, "r")
    # open outfile for writing
    file_name = args.OUTFILE
    fh_out = get_fh(file_name, 'w')
    # parse input file and write to oufile
    list_headers, list_seqs = get_header_and_seq_lists(fh_in)
    _check_size_of_lists(list_headers, list_seqs)
    print_sequence_stats(list_headers, list_seqs, fh_out)
    
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

def _get_number(header_string):
    """Returns line number"""
    count = 0
    number = []
    for line in header_string:
        line = line.split()
        count = count + 1
        number.append(count)
    return number

def _get_accession(header_string):
    """Returns the accession number of header"""
    accession = []
    for line in header_string:
        line = line.split()
        header = line[0]
        header = header.split('>')
        new_header = header[1]
        accession.append(new_header)
    return accession

def _get_nt_occurrence(character, seq_data):
    """Returns nucleotide count from sequence"""
    nuc_count = []
    bases = ["A", "T", "C", "G", "N"]
    if character in bases:
        pass
    else:
        sys.exit("Did not code this condition")

    for i, seq_string in enumerate(seq_data):
        if character in seq_string:
            nucleotides = seq_string.count(character)
            nuc_count.append(nucleotides)
    return nuc_count

def _get_seq_length(seq_data):
    """Return length of sequence"""
    length = []
    for i, seq_string in enumerate(seq_data):
        count = len(seq_string)
        length.append(count)
    return length

def _get_gc_content(seq_data):
    """Returns GC content of seq"""
    gc_cont = []
    total_nucs = 0
    total_gc = 0
    for i, seq_string in enumerate(seq_data):
        if "A" in seq_string:
            total_nucs += 1
        if "T" in seq_string:
            total_nucs += 1
        if "G" in seq_string:
            total_nucs += 1
            total_gc += 1
        if "C" in seq_string:
            total_nucs += 1
            total_gc += 1
        if "N" in seq_string:
            total_nucs += 1
        gc_content = (total_gc/total_nucs) * 100
        gc_cont.append(gc_content)
    return gc_cont

def print_sequence_stats(list_headers, list_seqs, fh_out):
    """Prints sequence stats"""
    number = _get_number(list_headers)
    accession = _get_accession(list_headers)
    get_a = _get_nt_occurrence('A', list_seqs)
    get_g = _get_nt_occurrence('G', list_seqs)
    get_t = _get_nt_occurrence('T', list_seqs)
    get_c = _get_nt_occurrence('C', list_seqs)
    get_n = _get_nt_occurrence('N', list_seqs)
    get_length = _get_seq_length(list_seqs)
    get_gc_cont = _get_gc_content(list_seqs)
    
    out = ("Number", "Accession", "A's", "G's", "T's", "C's", "N's", "Length", "GC%")
    fh_out.write("\t".join(out)+"\n")
    results = ('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(number, accession, get_a, get_g, get_t, get_c, get_n, get_length, get_gc_cont))
    fh_out.write(results)

def get_cli_args():
    """
    void: get_cli_args()
    Takes: no arugments
    Returns: instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Give the fasta\
sequence file name to get the nucleotide statistics')
    parser.add_argument('-i', '--infile', dest='INFILE',
                        type=str, help='Path to the file to open', required=True)
    parser.add_argument('-o', '--outfile', dest='OUTFILE',
                        type=str, help='Path to the file to write', required=True)
    return parser.parse_args()

if __name__ == "__main__":
    main()
