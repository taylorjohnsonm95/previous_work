#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 20:37:13 2020

@author: taylorjohnson
"""
import sys

sequence_name = input("Please enter a name for the DNA sequence: ")
print("Your sequence name is: {}".format(sequence_name))
length = input("please enter the length of the sequence: ")
print("The length of the sequence is: {}".format(length))

#Check to see if input is divisible by 3
if int(length) % 3 == 0:
    length_protein = int(length) / 3
    print("The length of the decoded protein is: {}".format(length_protein))
else:
    print("Error: the DNA sequence is not a multiple of 3")
    sys.exit(1) 
#Calculate weight in kilodaltons
kilodalton = (length_protein * 110) / 1000
print("The average weight of the protein sequence is: {}".format(kilodalton))

