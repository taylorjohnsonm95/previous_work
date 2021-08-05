#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:14:14 2020

@author: taylorjohnson
"""
import os
import pytest
from nucleotide_statistics_from_fasta import (get_fh, get_header_and_seq_lists,
                                              _check_size_of_lists, _get_nt_occurrence,
                                              _get_accession, _get_number,
                                              _get_seq_length)
file_test = 'test.txt'
file_test_input = ''
file_test_parsing = 'test.fasta'
fasta_string = """\
>EU521893 A/Arequipa/FLU3833/2006 2006// 4 (HA)
AACAGCACGGCAACGCTGTGCCTTGGGCACCANGCAGTACCAAACGGAACGATAGTGAAAACAATCACGA
ATGACCAAATTGAAGTTACTAATGCTACTGAGCTGGTTCAGAGTTCCTCAACAGGTGAAATATGCGACAG
TCCTCATCAGATCCTTGATGGAGAAAACTGCACACTAATAGATGCTCTATTGGGAGACCCTCAGTGTGAT
>EU521806 A/Arequipa/FLU3836/2006 2006// 4 (HA)
ATAAAAGCAACCAAAATGAAAGTAAAACTACTGGTTCTGTTATGTACATTTACAGCTACATATGCAGACA
TTTGGAGCCATTGCCGGTTTCATTGAAGGGGGGTGGACTGGAATGGTAGATGGTTGGTATGGTTATCATC
ATCAGAA
>EU521894 A/Arequipa/FLU3845/2006 2006// 4 (HA)
ACGGCAACGCTGTGCCTTGGGCACCATGCAGTACCAAACGGAACGATAGTGAAAACAATCACGAATGACC
AGACCCAGAGTAAGGAATATCCCCAGCAGAATAAGCATCTATTGGACAATAGTAAAACCGGGAGACATAC
>EU521895 A/Arequipa/FLU3846/2006 2006// 4 (HA)
GACAACAGCACGGCAACGCTGTGCCTTGGGCACCATGCAGTACCAAACGGAACGATAGTGAAAACAATCA
CGAATGACCAAATTGAAGTTACTAATGCTACTGAGCTGGTTCAGAGTTCCTCAACAGGTGAAATATGCGA
CAATCCTCATCAGATCCTTGATGGAGAGAACTGCACACTAATAGATGCTCTATTGGGAGACCCTCAGTGT
"""
file_test_stats = 'test.nucleotide_statistics_from_fasta.txt'


def test_get_fh_reading():
    # does it open file?
    _create_test_file(file_test)
    test = get_fh(file_test, 'r')
    # able to open for reading
    assert hasattr(test, 'readline') == True, "Able to open for reading"
    test.close()
    os.remove(file_test)
    

def test_get_fh_writing():
    # does it open file?
    test = get_fh(file_test, 'w')
    # able to open for reading
    assert hasattr(test, 'write') == True, "Able to open for writing"
    test.close()
    os.remove(file_test)
    

def test_get_fh_IOError():
    # does it raise IOError?
    with pytest.raises(IOError):
        get_fh('does_not_exist.txt', 'r')
        
        
#def test_get_fh_ValueError():
    # does it raise ValueError?
 #   _create_test_file(file_test)
  #  with pytest.raises(ValueError):
   #     get_fh('does_not_exist.txt", 'rrr')
    #os.remove(file_test)


def test__check_size_of_lists_different():
    # check lists that are different in size
    with pytest.raises(SystemExit):
        _check_size_of_lists([1,2,3], [1,2])
        

def test__check_size_of_lists_same():
    # check lists that are same in size
    assert _check_size_of_lists([1,2,3], [1,2,3]) == True, "Found same number of elements in list"
    
    
def test_get_header_and_seq_lists():
    # check data in each list
    _create_test_fasta_file()
    fh_in = get_fh(file_test_parsing, 'r')
    headers, seqs = get_header_and_seq_lists(fh_in)
    assert isinstance(headers, list) == True
    assert isinstance(seqs, list) == True 
    
    assert len(headers) == 4, "list of headers is 4"
    assert len(seqs) == 4, "list of sequences is 4"

    os.remove(file_test_parsing)


def test__get_nt_occurrence():
    # check each nuc has correct count
    assert _get_nt_occerrence('A', 'AATTGGCCN') == 2, "Found right number of A's"
    assert _get_nt_occurrence('G', 'AATTGGCCN') == 2, "Found right number of G's"
    assert _get_nt_occurrence('C', 'AATTGGCCN') == 2, "Found right number of C's"
    assert _get_nt_occurrence('T', 'AATTGGCCN') == 2, "Found right number of T's"
    assert _get_nt_occurrence('N', 'AATTGGCCN') == 1, "Found right number of N's"
    
    with pytest.raises(SystemExit):
        assert _get_nt_occurrence('Z', 'AATTGGCCN')
        
        
def test__get_accession():
    # check the accession is correct 
    _create_test_fasta_file()
    fh_in = get_fh(file_test_parsing, 'r')
    list_headers = get_header_and_seq_lists(fh_in)
    accession = _get_accession(list_headers)
    assert accession[0] == 'EU521893', "Got the accession number"
    assert isinstance(accession, list) == True, "Get true for accession list type"
    assert _get_accession('') == '', "Didn't get accession"

def test__get_number():
    # check the number is correct
    _create_test_fasta_file()
    fh_in = get_fh(file_test_parsing, 'r')
    list_headers = get_header_and_seq_lists(fh_in)
    number = _get_number(list_headers)
    assert number[0] == 1, "Got the number"
    assert isinstance(number, list) == True, "Get true for number list type"
    

def test__get_seq_length():
    # check seq length is correct
    _create_test_fasta_file()
    fh_in = get_fh(file_test_parsing, 'r')
    list_seqs = get_header_and_seqs(fh_in)
    length = _get_seq_length(list_seqs)
    assert length[0] == 210, "Got the length"
    assert isinstance(length, list) == True, "Get true for length list type"
    
    
def _create_test_file(file):
    open(file, 'w').close()
    

def _create_test_fasta_file():
    fh = open(file_test_parsing, 'w')
    fh.write(fasta_string)
    fh.close()
