#!/usr/bin/env bash

bwa mem -M -t 8 -R "@RG\tID:SRR6808334\tSM:bar" \
GRCh38_reference.fa \
SRR6808334_1.paired.fastq SRR6808334_2.paired.fastq \
1>SRR6808334.sam 2>aignReads.err &

# -R adding read groups
# -M mark shorter split hits

# bwa mem -M -t 8 -R "@RG\tID:SRR6808334\tSM:bar" \
# GRCh38_reference.fa \
# SRR6808334_1.unpaired.fastq \
# 1>SRR6808334_1.unpaired.sam 2>alignReads2.err &
  
# bwa mem -M -t 8 -R "@RG\tID:SRR6808334\tSM:bar" \
# GRCh38_reference.fa \
# SRR6808334_2.unpaired.fastq \
# 1>SRR6808334_2.unpaired.sam 2>alignReads3.err &
