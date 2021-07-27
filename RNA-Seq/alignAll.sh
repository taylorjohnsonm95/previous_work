#!/usr/bin/env bash
#alignAll.sh

# Initialize variable to contain the directory of trimmed fastq files 
fastqPath="/home/johnson.ta/BINF6308/RNA-Seq/Paired/"
# Initialize variable to contain the suffix for the left reads
leftSuffix=".R1.fastq"
rightSuffix=".R2.fastq"
pairedOutPath="sam/"

#create output directory
mkdir -p $pairedOutPath
#loop through left-read fastq files
function alignAll {
for leftInFile in $fastqPath*$leftSuffix
do
#remove path from filename
pathRemoved="${leftInFile/$fastqPath/}"
#remove left-read suffix from $pathRemoved
sampleName="${pathRemoved/$leftSuffix/}"

#align files to reference genome 
nice -n19 gsnap \
-A sam \
-D . \
-d AiptasiaGmapDb \
-s AiptasiaGmapIIT.iit \
$fastqPath$sampleName$leftSuffix \
$fastqPath$sampleName$rightSuffix \
"Paired/${sampleName}.R1.paired.fastq" \
"Paired/${sampleName}.R2.paired.fastq" \
1>"sam/${sampleName}.sam" 
done
}
alignAll 1>alignAll.log 2>alignAll.err &
