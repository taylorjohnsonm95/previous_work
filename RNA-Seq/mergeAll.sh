#!/usr/bin/env bash
#mergeAll.sh

#List the files with ls and redirect output to bamIn.txt
ls bam/Aip*.sorted.bam > bamIn.txt

samtools merge\
 -b bamIn.txt bam/AipAll.bam \
1>bam/merge.log 2>bam/merge.err &
