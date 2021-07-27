#!/usr/bin/env bash
#trinityDeNovo1.sh

#Get list of left reads and store as $leftReads
leftReads="$(ls -q Paired/Aip*.R1.fastq)"
#Store echo of $leftReads as $leftReads to get rid of line breaks
leftReads=$(echo $leftReads)
#Replace spaces in list of reads with comma
leftReads="${leftReads// /,}"

#Get list of right reads and store as $rightReads
rightReads="$(ls -q Paired/Aip*.R2.fastq)"
#Store echo of $rightReads as $rightReads to get rid of line breaks
rightReads=$(echo $rightReads)
#Replace spaces in list of reads with comma
rightReads="${rightReads// /,}"

nice -n19 /usr/local/programs/trinityrnaseq-Trinity-v2.8.4/Trinity \
--seqType fq \
--output trinity_de-novo \
--max_memory 10G --CPU 4 \
--left $leftReads \
--right $rightReads \
1>trinity_dn.log 2>trinity_dn.err &

