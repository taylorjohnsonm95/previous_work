#!/bin/bash

#$ -cwd
#$ -N binning
#$ -pe smp 30
#$ -q compute.q

. /etc/profile.d/modules.sh
module load default-environment
module load metabat/2.12.1
module load python/3.6.9
module load vamb/3.0.2

OUTDIR=./binned
mkdir -p ${OUTDIR}

jgi_summarize_bam_contig_depths --outputDepth ./align/depth.txt \
   ./align/*.aligned.sorted.duplicates_removed.bam

vamb -o '.' --outdir ${OUTDIR} --fasta ./assembly/catalogue.fna \
    --jgi ./align/depth.txt --minfasta 200000 
