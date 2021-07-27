#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: taylorjohnson
"""

import os
import pytest
from pdb_fasta_splitter import (get_fh, get_header_and_seq_lists, get_protein_and_ss_files, 
                                _check_size_of_lists)

file_test = 'test.txt'
file_test_input = ''
file_test_parsing = 'test.fasta'
fasta_string = """\
>101M:A:sequence
MVLSEGEWQLVLHVWAKVEADVAGHGQDILIRLFKSHPETLEKFDRVKHLKTEAEMKASEDLKKHGVTVLTALGA
ILKKKGHHEAELKPLAQSHATKHKIPIKYLEFISEAIIHVLHSRHPGNFGADAQGAMNKALELFRKDIAAKYKEL
GYQG
>101M:A:secstr
    HHHHHHHHHHHHHHGGGHHHHHHHHHHHHHHH GGGGGG TTTTT  SHHHHHH HHHHHHHHHHHHHHHH
HHTTTT  HHHHHHHHHHHHHTS   HHHHHHHHHHHHHHHHHH GGG SHHHHHHHHHHHHHHHHHHHHHHHHT
T
>102L:A:sequence
MNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAA
VRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSRWYNQTPNRAKRV
ITTFRTGTWDAYKNL
>102L:A:secstr
  HHHHHHHHH  EEEEEE TTS EEEETTEEEESSS TTTHHHHHHHHHHTS  TTB  HHHHHHHHHHHHHHH
HHHHHH TTHHHHHHHS HHHHHHHHHHHHHHHHHHHHT HHHHHHHHTT HHHHHHHHHSSHHHHHSHHHHHHH
HHHHHHSSSGGG
"""

file_test_protein_printing = 'test.protein.fasta'
file_test_ss_printing = 'test.ss.fasta'

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
    

def test_get_protein_and_ss_files():
    # check right data is printed
    _create_test_fasta_file()
    fh_in = get_fh(file_test_parsing, 'r')
    headers, seqs = get_header_and_seq_lists(fh_in)
    num_proteins, num_ss = get_protein_and_ss_files(headers, seqs,
                                                    get_fh(file_test_protein_printing, 'w'),
                                                    get_fh(file_test_ss_printing, 'w'))
    
    assert num_proteins == 2, "Number of proteins is 2"
    assert num_ss == 2, "Number of secondary structures is 2"
    
    os.remove(file_test_parsing)
    os.remove(file_test_protein_printing)
    os.remove(file_test_ss_printing)
    

def _create_test_file(file):
    open(file, 'w').close()
    

def _create_test_fasta_file():
    fh = open(file_test_parsing, 'w')
    fh.write(fasta_string)
    fh.close()



