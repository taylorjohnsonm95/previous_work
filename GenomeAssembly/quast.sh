#!/usr/bin/env bash
#quast.sh


#create output directory
pairedOutPath="Rhodo/"

#loop through fastq files
function quast {

#align files to reference genome 
nice -n19 /usr/local/programs/quast-4.6.3/quast.py \
-o $pairedOutPath --threads 4 \
"Rhodo/contigs.fasta" \
 --scaffolds \

}

quast 1>quast.log 2>quast.err &
