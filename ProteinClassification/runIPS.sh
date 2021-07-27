#!/usr/bin/env bash
#runIPS.sh

#run interproscan with proteins.fasta as input
function interproscan {

nice -n19 interproscan.sh \
    -i proteins.fasta \
    -o proteins.tsv \
    -f TSV \

}

interproscan 1>interproscan.log 2>interproscan.err &



