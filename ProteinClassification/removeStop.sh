#!/usr/bin/env bash
#removeStop.sh

#use sed to remove * and output first 500 lines to proteins.fasta 

sed 's/*//' \
    ../BLAST/Trinity.fasta.transdecoder.pep | head -n 500 > proteins.fasta \




    
