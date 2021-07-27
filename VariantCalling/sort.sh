#!/usr/bin/env bash

samtools sort -@ 8 -m 4G SRR6808334.sam -o SRR6808334.sorted.bam \
1>sort.log 2>sort.err

# sam = BAM
# -m 4G : set maximum memory per thread

# ln -s /data/METHODS/Spring/Module05/SRR6808334.sam SRR6808334.sam
