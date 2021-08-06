#!/bin/bash

#$ -cwd
#$ -N concatenate
#$ -pe smp 30
#$ -q compute.q


. /etc/profile.d/modules.sh
module load default-environment
module load python/3.6.9
module load vamb/3.0.2
module load intel-tbb-oss/intel64/2017_20160722oss
module load bowtie2/2.3.2

concatenate.py catalogue.fna.gz ./assembly/*/renamed.final.contigs.fa

gzip -d catalogue.fna.gz

bowtie2-build --threads 16 catalogue.fna MAGS


