#!/usr/bin/env bash

bwa index -a bwtsw GRCh38_reference.fa \
1>indexGenomeBwa.log 2>indexGenomeBwa.err

# ln -s /data/METHODS/Spring/Module05/GRCh38_reference.fa.sa GRCh38_reference.fa.sa
# ln -s /data/METHODS/Spring/Module05/GRCh38_reference.fa.amb GRCh38_reference.fa.amb
# ln -s /data/METHODS/Spring/Module05/GRCh38_reference.fa.ann GRCh38_reference.fa.ann
# ln -s /data/METHODS/Spring/Module05/GRCh38_reference.fa.pac GRCh38_reference.fa.pac
# ln -s /data/METHODS/Spring/Module05/GRCh38_reference.fa.bwt GRCh38_reference.fa.bwt

samtools faidx GRCh38_reference.fa \
1>indexGenomeSamtools.log 2>indexGenomeSamtools.err

# create .fai file
# ln -s /data/METHODS/Spring/Module05/GRCh38_reference.fa.fai GRCh38_reference.fa.fai
