!#/usr/bin/env bash

# retrieve NGS reads from NA12878 reference sample

fastq-dump --split-files SRR6808334 1>getReads.log 2>getReads.err

#ln -s /data/METHODS/Spring/Module05/SRR6808334_1.fastq SRR6808334_1.fastq
#ln -s /data/METHODS/Spring/Module05/SRR6808334_1.fastq SRR6808334_2.fastq
