#!/usr/bin/env bash

samtools index -@ 8 -m 4G -b SRR6808334.sorted.bam \
1>index.log 2>index.err

# ln -s /data/METHODS/Spring/Module05/SRR6808334.sorted.bam.bai SRR6808334.sorted.bam.bai
