#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 09:06:08 2020

@author: taylorjohnson
"""


sequence = "../assignment1/sequence.fasta.txt"

#Open file with amino acid sequence
with open(sequence, 'r') as seq:
    amino_acids= ''
    count = 0
    for line in seq:
        if line.startswith('>'):
            continue
        else:
            amino_acids = line.strip()
            count += len(amino_acids)
    #Calculate weight in kilodaltons         
    kilodaltons = (count * 110) /1000
    print('The length of "Protein kinase C beta type" is: {} \
          \nThe average weight of this protein sequence in kilodaltons is: {}'.format(count, kilodaltons))
    


