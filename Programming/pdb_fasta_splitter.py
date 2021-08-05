#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 18:21:19 2020

@author: taylorjohnson
"""
import sys
import argparse
def main():
    # figure out what the input filename is
    args = get_cli_args()
    file_name = args.INFILE

    # read the input FASTA file
    fh_in = get_fh(file_name, "r")

    # parse the input file and write to the output files
    list_headers, list_seqs = get_header_and_seq_lists(fh_in)
    _check_size_of_lists(list_headers, list_seqs)
    fh_out1, fh_out2 = get_protein_and_ss_files(list_headers, list_seqs)

def get_fh(file_name, mode):
    """Open a file for reading or writing"""
    # print(file_name + " " + mode)
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
        if line.startswith(">"):
            list_headers.append(line.strip())
            if sequences != '':
                list_seqs.append(sequences)
            sequences = ''
        else:
            sequences += line.strip()
    list_seqs.append(sequences.strip())
    list_check = _check_size_of_lists(list_headers, list_seqs)
    return list_headers, list_seqs

def get_protein_and_ss_files(list_headers, list_seqs):
    """Writes headers and sequences to two files"""
    fh_out1 = get_fh('pdb_protein.fasta', 'w')
    fh_out2 = get_fh('pdb_ss.fasta', 'w')
    index = 0
    for line in list_headers:
        if 'sequence' in line:
            fh_out1.write(list_headers[index])
            fh_out1.write(list_seqs[index])
            index += 1
        else:
            fh_out2.write(list_headers[index])
            fh_out2.write(list_seqs[index])
            index += 1
    print("Found {} protein sequences\nFound {} ss sequences".format(int(index/2), int(index/2)))
    return fh_out1, fh_out2

def get_cli_args():
    """
    void: get_cli_args()
    Takes: no arugments
    Returns: instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Give the fasta sequence file name to do the splitting')
    parser.add_argument('-i', '--infile', dest='INFILE',
                        type=str, help='Path to the file to open', required=True)
    return parser.parse_args()

if __name__ == "__main__":
    main()
