#!/usr/bin/env bash
#pfamScan.sh

nice -n19 hmmscan --cpu 4 --domtblout pfam.domtblout \
    /scratch/SampleDataFiles/Pfam-A.hmm \
    Trinity.fasta.transdecoder_dir/longest_orfs.pep \
    1>pfamScan.log 2>pfamScan.err &

