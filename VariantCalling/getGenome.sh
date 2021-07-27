!#/usr/bin/env bash

# get the GRCH38 reference genome

wget -c ftp://ftp.ebi.ac.uk/pub/database/gencode/Gencode_human/release_27/GRCh38.primary_assembly.genome.fa.gz \
    -O GRCh38_reference.fa.gz \
    1>getGenome.log 2>getGenome.err

gunzip GRCh38_reference.fa.gz

# ln -s/data/METHODS/Spring/Module05/GRCh38_reference.fa GRCh38_reference.fa
