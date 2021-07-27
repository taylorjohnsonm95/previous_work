#!/usr/bin/env bash
#trim.sh

#initialize variable to contain directory of un-trimmed fastq files
fastqPath="/home/johnson.ta/BINF6308/GenomeAssembly/"

#initialize variable to contain paired and unpaired reads
leftSuffix="SRR522244_1.fastq"
rightSuffix="SRR522244_2.fastq"
pairedOutPath="Paired/"
unpairedOutPath="Unpaired/"

#create output directories
mkdir -p $pairedOutPath
mkdir -p $unpairedOutPath

#loop through left-read fastq files in $fastqPath
function trim {
#trim sequences in files 
nice -n19 java -jar /usr/local/programs/Trimmomatic-0.36/trimmomatic-0.36.jar PE \
-threads 1 -phred33 \
$fastqPath$leftSuffix \
$fastqPath$rightSuffix \
$pairedOutPath$leftSuffix \
$unpairedOutPath$leftSuffix \
$pairedOutPath$rightSuffix \
$unpairedOutPath$rightSuffix \
HEADCROP:0 \
ILLUMINACLIP:/usr/local/programs/Trimmomatic-0.36/adapters/TruSeq3-PE.fa:2:30:10 \
LEADING:20 TRAILING:20 SLIDINGWINDOW:4:30 MINLEN:36

}
trim 1>trim.log 2>trim.err &

