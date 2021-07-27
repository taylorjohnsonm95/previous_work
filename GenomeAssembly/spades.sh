#!/usr/bin/env bash
#spades.sh

#create output directory
pairedOutPath="Rhodo/"

mkdir -p $pairedOutPath
#loop through fastq files
function spades {

#align files to reference genome 
nice -n19 /usr/local/programs/SPAdes-3.10.0-Linux/bin/spades.py \
-o $pairedOutPath --threads 4 \
-1 "Paired/SRR522244_1.fastq" \
-2 "Paired/SRR522244_2.fastq" \

}

spades 1>spades.log 2>spades.err &
