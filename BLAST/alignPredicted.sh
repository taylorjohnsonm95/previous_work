#!/usr/bin/env bash
#alignPredicted.sh


blastp -query Trinity.fasta.transdecoder.pep \
    -db swissprot -max_target_seqs 1 \
    -outfmt "6 qseqid sacc qlen slen length nident pident evalue < 1e-10 stitle" \
    1>alignPredicted.txt 2>alignPredicted.err &
