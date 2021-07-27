#!/usr/bin/env python3
import sys
import re

def sliding_window(kmer_size, fasta):
    """ return a list of all k-mers in given string """
    kmers = []
    seq =''
    with open(fasta, 'r') as file:
        for lines in file:
            if ">" in lines:
                print(lines.strip())
            else:
                seq += lines.strip()
    end = len(seq) - kmer_size + 1 
    for start in range(0, end):
        kmers.append(seq[start:start + kmer_size])
    return kmers

def gc_content(dna):
    """returns GC content of DNA"""
    dna = dna.lower()
    gc = 0
    for nucleotide in dna:
        if nucleotide in ['g', 'c']:
            gc += 1
    return gc/len(dna)


if __name__ == "__main__":
    #check for two arguments
    arg_count = len(sys.argv) - 1
    if arg_count < 2:
        raise Exception("This requires 2 arguments.")
    else:
        kmer_size= int(sys.argv[1])
        fasta = sys.argv[2]
        kmers = sliding_window(kmer_size, fasta)
        for i in range(len(kmers)):
            dna = kmers[i]
            result = gc_content(dna)
            print("{}\t{:.2f}".format(dna, result)) 





