#!/usr/bin/env bash
#alignPredicted.sh
#test

blastp -query Trinity.fasta.transdecoder.pep \
    -db swissprot -max_target_seqs 1 \
    -outfmt 6 \
    1>alignPredicted.txt 2>alignPredicted.err &
